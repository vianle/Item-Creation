import pymel.core as pm
import maya.cmds as cmds

#sliders
cmds.window('Lantern Maker')
cmds.columnLayout( adjustableColumn=True )
cmds.text('Enter values to make lantern')
ridgesSlider = cmds.intSliderGrp(l='Ridges',min=0, max=100, value=50, field=True)
deformSlider = cmds.intSliderGrp(l='Deform',min=0, max=100, value=1, field=True)
bendSlider = cmds.intSliderGrp(l='Bend',min=0, max=100, value=20, field=True)
flattenSlider = cmds.intSliderGrp(l='Flatten',min=0, max=100, value=0, field=True)
lanternButton = cmds.button(l='Make Lantern', c='makeLantern()')
cmds.showWindow()

def makeLantern():
	#clear workspace
	cmds.select(all=True)
	cmds.delete()
	
	#get values from sliders
	ridges = cmds.intSliderGrp(ridgesSlider, q=True, value=True)
	deform = cmds.intSliderGrp(deformSlider, q=True, value=True)
	bend = cmds.intSliderGrp(bendSlider, q=True, value=True)
	bendNum = bend/100.0+1.0
	flatten = float(cmds.intSliderGrp(flattenSlider, q=True, value=True))

	
	lantern = pm.polySphere(n='lantern', sx=10, r=1, sy=ridges)
	rings = pm.polySelect( lantern, er=1)
	pm.select(lantern, cl=True)
	toggle = True
	for i in rings:
	    if toggle:
	        pm.polySelect( lantern, el=i)
	        pm.scale(pm.selected(), [bendNum,bendNum,bendNum], xz=True)
	    toggle = not toggle
	pm.select(lantern)
	pm.displaySmoothness(divisionsU=3, divisionsV=3, pointsWire=16, pointsShaded=4, polygonObject=3)
	wave = pm.nonLinear(type='wave', amplitude=0.03)
	pm.setAttr(wave[0]+'.wavelength', deform/100+0.1)
	pm.rotate(wave, 0, 0, '45deg')
	pm.select(all=True)
	pm.scale(lantern, [1,1-(flatten/100),1], xyz=True)
	pm.delete(ch=True)
	

