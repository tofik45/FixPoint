import PySimpleGUI as sg
import os

sg.theme('Default1')
OUTFILE = 'tmp.nc1'
FIND = '...'

layout = [
	[sg.InputText(), sg.FileBrowse('...', key = '-FILE-') ],
	[sg.Button('Исправить')]
]

window = sg.Window('Исправление позиций для V808', layout)
while True:
	event, values = window.read()
	if event == sg.WIN_CLOSED: 
		break
	elif event == 'Исправить':
		with open(values['-FILE-']) as infile, open(OUTFILE, 'w') as outfile:
			for line in infile:
				numbers = int(line.split())

				#if numbers > 12000 or numbers < -12000:

				if FIND not in line:
					outfile.write(line)
		os.remove(values['-FILE-'])
		os.rename(OUTFILE, values['-FILE-'])


		

window.close()