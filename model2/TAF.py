class TafReport:
    def __init__(self, tafId, icaoId, dbPopTime, bulletinTime, issueTime, validTimeFrom, validTimeTo, 
                 rawTAF, mostRecent, remarks, lat, lon, elev, prior, name, fcsts):
        self.tafId = tafId
        self.icaoId = icaoId
        self.dbPopTime = dbPopTime
        self.bulletinTime = bulletinTime
        self.issueTime = issueTime
        self.validTimeFrom = validTimeFrom
        self.validTimeTo = validTimeTo
        self.rawTAF = rawTAF
        self.mostRecent = mostRecent
        self.remarks = remarks
        self.lat = lat
        self.lon = lon
        self.elev = elev
        self.prior = prior
        self.name = name
        self.fcsts = [TafForecast(**fcst) for fcst in fcsts] if fcsts else []

    def __repr__(self):
        return f"TafReport({self.icaoId}, Valid: {self.validTimeFrom} - {self.validTimeTo})"

class TafForecast:
    def __init__(self, timeGroup, timeFrom, timeTo, timeBec, fcstChange, probability, wdir, wspd, wgst, 
                 wshearHgt, wshearDir, wshearSpd, visib, altim, vertVis, wxString, notDecoded, clouds, 
                 icgTurb, temp):
        self.timeGroup = timeGroup
        self.timeFrom = timeFrom
        self.timeTo = timeTo
        self.timeBec = timeBec
        self.fcstChange = fcstChange
        self.probability = probability
        self.wdir = wdir
        self.wspd = wspd
        self.wgst = wgst
        self.wshearHgt = wshearHgt
        self.wshearDir = wshearDir
        self.wshearSpd = wshearSpd
        self.visib = visib
        self.altim = altim
        self.vertVis = vertVis
        self.wxString = wxString
        self.notDecoded = notDecoded
        self.clouds = [CloudLayer(**cloud) for cloud in clouds] if clouds else []
        self.icgTurb = icgTurb if icgTurb else []
        self.temp = temp if temp else []

    def __repr__(self):
        return f"TafForecast(Time: {self.timeFrom} - {self.timeTo}, Wind: {self.wdir}° @ {self.wspd}kt, Visibility: {self.visib})"

class CloudLayer:
    def __init__(self, cover, base, type):
        self.cover = cover
        self.base = base
        self.type = type

    def __repr__(self):
        return f"CloudLayer({self.cover}, Base: {self.base} ft)"