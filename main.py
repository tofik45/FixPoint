import PySimpleGUI as sg
import os

sg.theme('Default1')
OUTFILE = 'tmp.nc1'

layout = [
	[sg.InputText(), sg.FileBrowse('...', key = '-FILE-') ],
	[sg.Button('Исправить')]
]

window = sg.Window('Исправление позиций', layout)
while True:
	event, values = window.read()
	if event == sg.WIN_CLOSED: 
		break
	elif event == 'Исправить':
		with open(values['-FILE-']) as infile, open(OUTFILE, 'w') as outfile:
			for line in infile:
				numbers = 0
				if line.startswith('   '):
					str_line = line.split()
					numbers = float(str_line[0])

				if numbers < 12000 and numbers > -12000:
					outfile.write(line)
				
		os.remove(values['-FILE-'])
		os.rename(OUTFILE, values['-FILE-'])

window.close()