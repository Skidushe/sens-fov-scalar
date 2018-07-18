import math

inputs = {}

inputs['wps'] = float(input("\nInput WPS Multiplier (6/11 = 1. 4/11 = 0.5, etc):  "))
inputs['vres'] = int(input("\nInput Vertical Pixels:  "))

inputs['maxFov'] = int(input("\nInput MAX fov to scale to (90 is default, don't go higher than ~130):  "))
inputs['minFov'] = int(input("\nInput MIN fov to scale to (don't go lower than ~10):  "))

def getSensValue(fov):
    yaw = 1000/22
    vfov = (360 * math.atan(3/4 * math.tan((math.pi * fov)/360)))/math.pi
    dfov = (360 * math.atan(math.sqrt(2) * math.tan((math.pi * vfov)/360)))/math.pi
    hfov169 = (360 * math.atan(16/9 * math.tan((math.pi * vfov)/360)))/math.pi
    hfov219 = (360 * math.atan(64/27 * math.tan((math.pi * vfov)/360)))/math.pi

    # viewspeed v1 - 1:1 diagonal
    # newSens = (90/fov) * (360 * yaw) / (4 * math.pi * (math.sqrt(2) * inputs['vres'] / inputs['wps'])) / (math.sin((math.pi * dfov)/360) / math.pow((math.pi * dfov)/180,2))

    # viewspeed v2 - 1:1
    newSens = (90/fov) * (360 * yaw) / (math.pi * (inputs['vres'] / inputs['wps'])) * math.sin((math.pi * vfov)/360)

    # viewspeed v2 - 1:1 diagonal
    # newSens = (90/fov) * (360 * yaw) / (math.pi * (inputs['vres'] / inputs['wps'])) * math.sin((math.pi * dfov)/360)

    # zoom ratio
    # newSens = (90/fov) * (360 * yaw) / ((((math.pi * inputs['vres']) / inputs['wps'])) / math.tan((math.pi * vfov)/360))

    # monitor match - 1:1 diagonal
    # newSens = (90/fov) * (360 * yaw) / ((((math.pi * math.sqrt(2) * inputs['vres']) / inputs['wps'])) * (360/math.pi / dfov))

    # monitor match - 1:1
    # newSens = (90/fov) * (360 * yaw) / ((((math.pi * inputs['vres']) / inputs['wps'])) * (360/math.pi / vfov))

    # monitor match - 4:3
    # newSens = (90/fov) * (360 * yaw) / ((((math.pi * 4/3 * inputs['vres']) / inputs['wps'])) * (360/math.pi / fov))

    # monitor match - 16:9
    # newSens = (90/fov) * (360 * yaw) / ((((math.pi * 16/9 * inputs['vres']) / inputs['wps'])) * (360/math.pi / hfov169))

    # monitor match - 21:9
    # newSens = (90/fov) * (360 * yaw) / ((((math.pi * 64/27 * inputs['vres']) / inputs['wps'])) * (360/math.pi / hfov219))

    return round(newSens, 16)


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
