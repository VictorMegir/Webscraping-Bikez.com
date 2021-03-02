def transform_lubrication(s):
    try:
        s = re.sub(r'\s+', ' ', s)
        s = s.strip(' ,.:\n\t\r')
        s = s.lower()
        s = s.replace('`', '')

        if 'wer sump' in s: s = s.replace('wer', 'wet')
        if 'forced/splash' in s: s = s.replace('forced/splash', 'forced and splash')
        if 'sump-pump' in s: s = s.replace('sump-pump', 'sump')
        if 'semi dry' in s: s = s.replace('semi dry', 'semi-dry')
        if 'summp' in s: s.replace('summp', 'sump')
        if 'sumpy' in s: s.replace('sumpy', 'sump')
        if s in ['none','(unspecified)','null',' ','-','wet','800ml','5%','6%','dry','0.9l','']: s = np.nan
        if len(s) == 1: s = np.nan
    
        return s
    except TypeError:
        return np.nan
    
#raw['Lubrication system'] = raw['Lubrication system'].apply(lambda row: transform_lubrication(row))


def transform_clutch(s):
    try:
        s = s.lower()
        s = s.strip(' ,.:\n\t\r')
        s = re.sub(r'\s+', ' ', s)
        s = re.sub(r'\s+/\s+', '/', s)
        s = s.replace('/ ', '/')
        s = s.replace('`', '')
        s = s.replace(',', '')
        s = s.replace(';', '.')
        s = s.replace(';', '.')
        s = s.replace('´', '')
        s = s.replace('™', '')

        if 'multi-plate' in s: s = s.replace('multi-plate', 'multiplate')
        if 'multi-disc' in s: s = s.replace('multi-disc', 'multidisc')
        if 'multi-disk' in s: s = s.replace('multi-disk', 'multidisc')
        if 'multiple-disc' in s: s = s.replace('multiple-disc', 'multidisc')
        if 'wetmultidisc' in s: s = s.replace('wetmultidisc', 'wet multidisc')
        if 'multiple plate' in s: s = s.replace('multiple plate', 'multiplate')
        if 'multidisc wet' in s: s = s.replace('multidisc wet', 'wet multidisc')
        if 'wet multidisc clutch' in s: s = s.replace('wet multidisc clutch', 'wet multidisc')
        if 'dry type' in s: s = s.replace('dry type', 'dry')
        if 'cluth' in s: s = s.replace('cluth', 'clutch')
        if 'dry clutch' in s: s = s.replace('dry clutch', 'dry')
        if 'wet clutch' in s: s = s.replace('wet clutch', 'wet')
        if 'clutch.' in s: s = s.replace('clutch.', 'clutch')
        if 'wet.' in s: s = s.replace('wet.', 'wet')
        if 'hidraulic' in s: s = s.replace('hidraulic', 'hydraulic')
        if 'hyrdaulically' in s: s = s.replace('hyrdaulically', 'hydraulically')
        if 'oil-bath' in s: s = s.replace('oil-bath', 'oil bath')
        if 'oil-bath.' in s: s = s.replace('oil bath.', 'oil bath')
        if s in ['none','(unspecified)','null',' ','-','wet','800ml','5%','6%','dry','0.9l','']: s = np.nan
        if len(s) == 1: s = np.nan
    
        return s
    except (TypeError, AttributeError):
        return np.nan
    
#raw['Clutch'] = raw['Clutch'].apply(lambda row: transform_clutch(row))

def extract_driveline(s):
    try:
        s = s.lower()
        s = s.strip(' ,.:\n\t\r')
        s = re.sub(r'\s+', ' ', s)
        s = re.sub(r'\s+/\s+', '/', s)
        s = s.replace('/ ', '/')
        s = s.replace('`', '')
        s = s.replace(',', '')
        s = s.replace(';', '.')
        s = s.replace('´', '')
        s = s.replace('™', '')
        s = s.replace('•', '')
        s = s.replace('®', '')
        
        s = re.sub(r"\d+\.\d+?", lambda mo: mo.group().replace('.','*'), s)
        s = re.sub(r"\d+\:\d+?", lambda mo: mo.group().replace(':','**'), s)
        s = s.replace('.', '')
        s = s.replace(':', '')
        
        s = s.replace('**', ':')
        s = s.replace('*', '.')
        
        if len(s) == 1: s = np.nan
    
        return s
    except (TypeError, AttributeError):
        return np.nan

#raw['Driveline'] = raw['Driveline'].apply(lambda row: extract_driveline(row))

def extract_emission(s):
    try:
        s = s.lower()
        s = s.strip(' ,.:\n\t\r')
        s = re.sub(r'\s+', ' ', s)
        s = re.sub(r'\s+/\s+', '/', s)
        s = s.replace('/ ', '/')
        s = s.replace(',', '')
        
        s = s.replace('sensors', 'sensor')
        s = s.replace('converters', 'converter')
        s = s.replace('resources', 'resource')
        s = s.replace('carb', 'c.a.r.b.')
        
        s = s.replace('eu-4', 'euro 4')
        s = s.replace('eu-5', 'euro 5')
        s = s.replace('eu- 5', 'euro 5')
        s = s.replace('eu5', 'euro 5')
        s = s.replace('euro iv', 'euro 4')
        s = s.replace('e4', 'euro 4')
        s = s.replace('eu4', 'euro 4')
        s = s.replace('euro4', 'euro 4')
        s = s.replace('eu 3', 'euro 3')
        s = s.replace('eu3', 'euro 3')
        s = s.replace('eu-3', 'euro 3')
        s = s.replace('euro3', 'euro 3')
        s = s.replace('euroiii', 'euro 3')
        s = s.replace('euro i3', 'euro 3')
        s = s.replace('euro ii', 'euro 2')
        s = s.replace('euro 2i', 'euro 2')
        
        s = s.replace('3-way', '3 way')
        s = s.replace('three-way', '3 way')
        s = s.replace('3 ways', '3 way')
        
        s = s.replace('exhaustemissionhc', 'exhaust emission hc')
        s = s.replace('exhaustemissionnox', 'exhaust emission nox')
        
        if len(s) == 1: s = np.nan
        if s in ['none', 'n/a', 'fornia']: s = np.nan
        if s == 'ch': s = 'hc'
        
        return s
    except (TypeError, AttributeError):
        return np.nan

#raw['Emission details'] = raw['Emission details'].apply(lambda row: extract_emission(row))