import win32com.client
import os

def change_text(path):
    psApp.Open(item)

    doc = psApp.Application.ActiveDocument

    import datetime
    layerText = doc.ArtLayers['date']
    text_of_layer = layerText.TextItem
    today = datetime.date.today()
    if today.weekday() == 6:
        today += datetime.timedelta(7)
    else:
        while today.weekday() != 6:
            today += datetime.timedelta(1)
    print(today.strftime('%m.%d.%Y'))
    text_of_layer.contents = today.strftime('%m.%d.%Y')

    #png save options
    options = win32com.client.Dispatch('Photoshop.ExportOptionsSaveForWeb')
    options.Format = 13   # PNG
    options.PNG8 = True  # Sets it to PNG-8 bit

    #new folder save location
    folder, filename = os.path.split( item )

    filename, ext = os.path.splitext( filename )
    filenamePng = filename + ".png"
    saveDir = r"C:\Users\nguye\Desktop\Live"
    newSave = os.path.join( saveDir, filenamePng )

    ##&& check to make sure file does not already exist

    doc.Export(ExportIn=newSave, ExportAs=2, Options=options)
    doc.Close(2)


psApp = win32com.client.Dispatch('Photoshop.Application')

EM = r"C:\Users\nguye\Desktop\Live\EM-YOUTUBE.psd"
VN = r"C:\Users\nguye\Desktop\Live\VN-YOUTUBE.psd"

path = [EM, VN]
for item in path:
    change_text(item)

psApp.Quit()