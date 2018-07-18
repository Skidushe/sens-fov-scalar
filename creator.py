import math

inputs = {}

inputs['sens'] = float(input("\nInput cs:go sensitivity:  "))
inputs['hres'] = int(input("\nInput resolution x:  ")) # So we can work out aspect ratio
inputs['vres'] = int(input("\nInput resolution y:  ")) # So we can work out aspect ratio
inputs['ratiomatch'] = float(input("\nInput monitor distance % match ratio:  "))

inputs['maxFov'] = int(input("\nInput MAX fov to scale to (90 is default, don't go higher than ~130):  "))
inputs['minFov'] = int(input("\nInput MIN fov to scale to (don't go lower than ~10):  "))

def getSensValue(fov):
    if inputs['ratiomatch'] != 0: #If 0, we don't need a lot of the extra computation, and won't work because division by 0
        conversionMethod = math.atan(((inputs['ratiomatch'] / 100) * (inputs['hres'] / inputs['vres'])) * math.tan((math.pi * (360 * math.atan(3/4 * math.tan((math.pi * fov)/360)))/math.pi) / 360)) / math.atan(((inputs['ratiomatch'] / 100) * (inputs['hres'] / inputs['vres'])) * math.tan((math.pi * (360 * math.atan(3/4 * math.tan((math.pi * 90)/360)))/math.pi) / 360))
    else:
        conversionMethod = math.tan((math.pi * (360 * math.atan(3/4 * math.tan((math.pi * fov)/360)))/math.pi) / 360) / math.tan((math.pi * (360 * math.atan(3/4 * math.tan((math.pi * 90)/360)))/math.pi) / 360)
    newSens = (90 / fov) * inputs['sens'] * conversionMethod # Calculate new sensitivity
    return round(newSens, 7)


with open('fovscale'+str(inputs['minFov'])+'+'+str(inputs['maxFov'])+'.cfg', 'w+') as f:
    if inputs['minFov'] < 90 < inputs['maxFov']:
        f.write('bind 1 "exec up_90"') # if 90 in range, we can start from default FOV so it will look a bit smoother
    else:
        f.write('bind 1 "exec up_'+str(inputs['minFov'])+'"')

for fov in range(inputs['minFov'],inputs['maxFov']+1):
    sens = str(getSensValue(fov))
    if fov != inputs['maxFov']:
        with open('up_'+str(fov)+'.cfg', 'w+') as f:
            f.write('fov_cs_debug '+str(fov)+'\n')
            f.write('sensitivity '+sens+'\n')
            f.write('bind 1 "exec up_'+str(fov+1)+'"\n')
    else:  # bind to start going backwards in FOV
        with open('up_'+str(fov)+'.cfg', 'w+') as f:
            f.write('fov_cs_debug '+str(fov)+'\n')
            f.write('sensitivity '+sens+'\n')
            f.write('bind 1 "exec down_'+str(fov-1)+'"\n')

    if fov != inputs['minFov']:
        with open('down_'+str(fov)+'.cfg', 'w+') as f:
            f.write('fov_cs_debug '+str(fov)+'\n')
            f.write('sensitivity '+sens+'\n')
            f.write('bind 1 "exec down_'+str(fov-1)+'"\n')
    else:  # bind to start going forwards in FOV 
        with open('down_'+str(fov)+'.cfg', 'w+') as f:
            f.write('fov_cs_debug '+str(fov)+'\n')
            f.write('sensitivity '+sens+'\n')
            f.write('bind 1 "exec up_'+str(fov+1)+'"\n')
