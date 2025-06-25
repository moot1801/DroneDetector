import numpy as np
import h5py

def to_string(x):
    decode_str = ''.join(chr(c[0]) for c in x)
    return decode_str


# h5py 파일을 불러와 필요한 데이터별로 구분하여 Dictionary 형태로 반환하는 함수
def h5pyToData(file_path):
    with h5py.File(file_path, 'r') as f:
        fc = f['Channel_1']
        ff = f['Frame']

        # Channel_1
        data = np.array(fc['Data'][:].flatten(), dtype=np.float64) #array([ -1644.,  -1208.,  -1032., ...,   6948., -24552., -32736.])
        numPoint = np.array(fc['NumPoints'][0][0], dtype=np.float64) # array(5000000.)
        numSegment = np.array(fc['NumSegments'][0][0], dtype=np.float64) # array(0.)
        waveFromType = np.array(to_string(fc['WaveformType'][:])) # array('NORMAL', dtype='<U6') 
        
            # x
        XData = np.array(fc['XData'], dtype=np.float64) # array([0., 0.])
        XDisOrigin = np.array(fc['XDispOrigin'][0][0], dtype=np.float64) # array(-0.0005)
        XDisRange = np.array(fc['XDispRange'][0][0], dtype=np.float64) # array(0.001)
        XInc = np.array(fc['XInc'][0][0], dtype=np.float64) # array(5.e-11)
        XOrg= np.array(fc['XOrg'][0][0], dtype=np.float64) # array(-0.000125)
        XUnits = np.array(to_string(fc['XUnits'])) # array('Second', dtype='<U6')
        
            # y
        YDisOrigin = np.array(fc['YDispOrigin'][0][0], dtype=np.float64) # array(-0.0005) # array(0.)
        YDisRange = np.array(fc['YDispRange'][0][0], dtype=np.float64) # array(0.40000001)
        YInc = np.array(fc['YInc'][0][0], dtype=np.float64) # array(6.58411815e-06)
        YOrg= np.array(fc['YOrg'][0][0], dtype=np.float64) # array(0.00663679)
        YUnits = np.array(to_string(fc['YUnits'])) # array('Volt', dtype='<U4')
        
        # Frame
        date = np.array(to_string(ff['Date'])) # array('29-Aug-2020  2:32:50', dtype='<U20')
        model = np.array(to_string(ff['Model'])) # array('MSOS604A', dtype='<U8')
        serial = np.array(to_string(ff['Serial']))

         # return 값들
        data = data.reshape(1, -1)
        data_ch = { 'NumPoints': [numPoint], 'NumSegments': [numSegment], 'WaveformType':[waveFromType]}
        data_xy = { 'XDisOrigin': [XDisOrigin], 'XDisRange': [XDisRange], 'XInc': [XInc], 'XOrg':[XOrg], 'XUnits': [XUnits], 'YDisOrigin':[YDisOrigin], 'YDisRange':[YDisRange], 'YInc': [YInc], 'YOrg':[YOrg], 'YUnits': [YUnits]}
        frame = {'Date': [date], 'Model':[model], 'Serial':[serial]}
    return [data, data_ch, data_xy, frame]

