from dirsync import sync
import PySimpleGUI as sg

def sync_folder(sourcedir, targetdir):
    sourcedir = sourcedir
    targetdir = targetdir
    sync(sourcedir, targetdir, "sync", verbose=True)
    sg.popup('同期が完了しました。')


def main_window():
    layout = [
        [sg.InputText(size=(50,1), key="-suourcedir-"), sg.FolderBrowse(button_text="コピー元を選ぶ")],
        [sg.InputText(size=(50,1), key="-targetdir-"), sg.FolderBrowse(button_text="コピー先を選ぶ")],
        [sg.Submit(button_text="開始")]
    ]
    window = sg.Window("フォルダ同期", layout=layout)

    while True:
        event, values = window.read()
        if event is None:
            break

        if event == "開始":
            sourcedir = values["-suourcedir-"]
            targetdir = values["-targetdir-"]
            sync_folder(sourcedir, targetdir)



if __name__ == "__main__":
    main_window()
# git テスト

#　追記