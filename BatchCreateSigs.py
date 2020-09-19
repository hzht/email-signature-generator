# version: 1.3
# date: 20 November 2019
import csv
import sys
import shutil

csvtoDict = {} #username: [displayName, title, fullAddr, city, state, pCode, ph, mob, fax, email, username]
errCount = 0
listofUsrErrs = []

with open('usernames.csv', newline='') as csvfile:
    entireList = csv.reader(csvfile, delimiter=',')
    for row in entireList:
        csvtoDict[row[10]] = [row[0], row[1], row[2], row[3], row[4], row[5], row[7], row[8], row[9], row[11], row[10]]

for i in csvtoDict:
    try:
        uName = csvtoDict[i][10] # username
        path = '\\\\<insert IP addr>\\profiles$\\{0}\\Managed Profile\\AppData\\Roaming\\Microsoft\\Signatures\\'.format(uName) # dependent on the path where user profiles are stored
        sig = open(str(uName) + '.htm', 'w')
        sig.write('<p style="font-family:Arial;font-size:10pt;font-weight:bold;margin:1px;">' + csvtoDict[i][0] + '</p>') # display name
        sig.write('<p style="font-family:Arial;font-size:10pt;margin:1px;">' + csvtoDict[i][1] + '</p>') # title
        sig.write('<p style="font-family:Arial;font-size:10pt;font-weight:bold;margin:1px;">' + 'My Company Name' + '</p>')
        sig.write('<p style="font-family:Arial;font-size:10pt;margin:1px;">&nbsp</p>')
        if csvtoDict[i][6] != '':
            sig.write('<p style="font-family:Arial;font-size:10pt;margin:1px;">' + '<b>P</b> ' + csvtoDict[i][6] + '</p>') # ph
        if csvtoDict[i][7] != '':
            sig.write('<p style="font-family:Arial;font-size:10pt;margin:1px;">' + '<b>M</b> ' + csvtoDict[i][7] + '</p>') # mob
        sig.write('<a style="font-family:Arial;font-size:10pt;margin:1px;" href="mailto:' + csvtoDict[i][9] + '">' + csvtoDict[i][9] + '</a>')
        sig.write('<p style="font-family:Arial;font-size:10pt;margin:1px;">' + csvtoDict[i][2] + ', ' + csvtoDict[i][4] + ', ' + csvtoDict[i][5] + '</p>') # fullAddr, state, pCode                
        sig.write('<a style="font-family:Arial;font-size:10pt;margin:1px;" href="http://www.mycompany.com.au/">mycompany.com.au</a>')

        sig.write('<p style="font-family:Arial;font-size:10pt;margin:1px;">&nbsp</p>')

        sig.write('<a href="https://www.facebook.com/companyname"><img src="fb.jpg" style="display:inline;padding-right:4px;"/></a>')
        sig.write('<a href="https://www.instagram.com/companyname"><img src="in.jpg" style="display:inline;padding-right:4px;"/></a>')
        sig.write('<a href="https://www.twitter.com/companyname"><img src="tw.jpg" style="display:inline;padding-right:4px;"/></a>')
        sig.write('<a href="https://www.youtube.com/companyname"><img src="yt.jpg" style="display:inline;padding-right:4px;"/></a>')

        sig.write('<p style="font-family:Arial;font-size:10pt;margin:1px;"><b>Visit our <a href="http://www.mycompany.com.au/">website</a> to find out about all of the exciting things you can do and see!</b></p>')
        
        sig.write('<p style="font-family:Arial;font-size:10pt;margin:1px;">&nbsp</p>')
        
        sig.write('<a href="https://www.mycompany.com.au/?id=email"><img src="https://www.mycompany.com.au/path-to-media/images/image.jpg" alt="365 things to do at My Company"></a>')
        
        sig.write('<p style="font-family:Arial;font-size:10pt;margin:1px;">&nbsp</p>')
        
        sig.write('<p style="font-family:Arial;font-size:8pt;margin:1px">The information that you voluntarily provide to the Company Name (Address) is collected</p>')
        sig.write('<p style="font-family:Arial;font-size:8pt;margin:1px">for administrative purposes and may be held in a database shared with the Parent Company Name.')
        sig.write('<p style="font-family:Arial;font-size;8pt;margin:1px">You have the right to access and correct the information.</p>')
        sig.close()
        
        shutil.copyfile(str(uName) + '.htm', path + 'signature.htm') # copy the sig
        shutil.copyfile('sigpic.jpg', path + 'sigpic.jpg')  # copy the sig image
        shutil.copyfile('fb.jpg', path + 'fb.jpg') # social media icons
        shutil.copyfile('in.jpg', path + 'in.jpg')
        shutil.copyfile('tw.jpg', path + 'tw.jpg')
        shutil.copyfile('yt.jpg', path + 'yt.jpg')
    except Exception: 
        print('ooops! ' + uName, sys.exc_info())
        errCount += 1
        listofUsrErrs.append(uName)
    finally:
        pass

print(errCount)
print(listofUsrErrs)
