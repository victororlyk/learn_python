import sqlite3

try:
    import tkinter
except ImportError:
    import Tkinter as tkinter


class Scrollbox(tkinter.Listbox):
    def __init__(self, window, **kwargs):
        super().__init__(window, **kwargs)
        self.scrollbar = tkinter.Scrollbar(window, orient=tkinter.VERTICAL,
                                           command=self.yview)

    def grid(self, row, column, sticky='nse', rowspan=1, columnspan=1,
             **kwargs):
        super().grid(row=row, column=column, sticky=sticky, rowspan=rowspan,
                     columnspan=columnspan, **kwargs)
        self.scrollbar.grid(row=row, column=column, sticky='nse',
                            rowspan=rowspan)
        self['yscrollcommand'] = self.scrollbar.set


class DataListBox(Scrollbox):
    def __init__(self, window, connection, table, field, sort_order=(),
                 **kwargs):
        super().__init__(window, **kwargs)
        self.linked_box = None
        self.linked_field = None
        self.link_value = None
        self.cursor = connection.cursor()
        self.table = table
        self.field = field

        self.bind('<<ListboxSelect>>', self.on_select)

        self.sql_select = "SELECT {},  _id FROM {}".format(self.field,
                                                           self.table)
        if sort_order:
            self.sql_sort = " ORDER BY " + ", ".join(sort_order)
        else:
            self.sql_sort = " ORDER BY " + self.field

    def clear(self):
        self.delete(0, tkinter.END)

    def link(self, widget, link_field):
        self.linked_box = widget
        widget.linked_field = link_field

    def requery(self, link_value=None):
        print(link_value, self.linked_box)
        self.link_value = link_value  # store the id so we know the 'master'
        # we are populating from
        if link_value and self.linked_field:
            sql = "{} WHERE {}=? {}".format(self.sql_select,
                                            self.linked_field, self.sql_sort)
            self.cursor.execute(sql, (link_value,))
        else:
            self.cursor.execute(self.sql_select + self.sql_sort)
        self.clear()
        for value in self.cursor:
            self.insert(tkinter.END, value[0])

        if self.linked_box:
            self.linked_box.clear()

    def on_select(self, event):
        if self.linked_box:
            index = self.curselection()[0]
            value = self.get(index),
            # get id from db
            if self.link_value:
                value = value[0], self.link_value
                sql_value = " WHERE {}=? and {} =?".format(self.field,
                                                           self.linked_field)
            else:
                sql_value = " WHERE {}=?".format(self.field)
            link_id = self.cursor.execute("{} {}".format(
                self.sql_select, sql_value), value).fetchone()[1]
            self.linked_box.requery(link_id)


if __name__ == '__main__':
    conn = sqlite3.connect('music.sqlite')

    mainWindow = tkinter.Tk()
    mainWindow.title("Music db browser")
    mainWindow.geometry('1024x760')

    mainWindow.columnconfigure(0, weight=2)
    mainWindow.columnconfigure(1, weight=2)
    mainWindow.columnconfigure(2, weight=2)
    mainWindow.columnconfigure(3, weight=1)

    mainWindow.rowconfigure(0, weight=1)
    mainWindow.rowconfigure(1, weight=5)
    mainWindow.rowconfigure(2, weight=5)
    mainWindow.rowconfigure(3, weight=1)

    # ------labels------
    tkinter.Label(mainWindow, text="Artists").grid(row=0, column=0)
    tkinter.Label(mainWindow, text="Albums").grid(row=0, column=1)
    tkinter.Label(mainWindow, text="Songs").grid(row=0, column=2)

    # ------Artists listboxes -----
    artistsList = DataListBox(mainWindow, conn, 'artists', 'name')
    artistsList.grid(row=1, column=0, sticky='news', rowspan=2, padx=(30, 0))
    artistsList.config(border=2, relief='sunken')
    artistsList.requery()
    # artistsList.bind('<<ListboxSelect>>', get_albums)

    # --------Albums Listbox -------
    albumLV = tkinter.Variable(mainWindow)
    albumLV.set(("Choose an artist",))
    albumList = DataListBox(mainWindow, conn, 'albums', 'name', sort_order=(
        'name',))
    # albumList.requery(12)
    albumList.grid(row=1, column=1, sticky="nsew", padx=(30, 0))
    albumList.config(border=2, relief="sunken")
    # albumList.bind('<<ListboxSelect>>', get_songs)
    artistsList.link(albumList, 'artist')
    # -----Song config ------
    songLV = tkinter.Variable(mainWindow)
    songLV.set(("Choose an album",))
    songList = DataListBox(mainWindow, conn, 'songs', 'title',
                           ('track', 'title'))
    # songList.requery()
    songList.grid(row=1, column=2, sticky='news', padx=(30, 0))
    songList.config(border=2, relief='sunken')

    albumList.link(songList, 'album')

    # --- main looop ----

    mainWindow.mainloop()
    print("closing db connection")
    conn.close()
