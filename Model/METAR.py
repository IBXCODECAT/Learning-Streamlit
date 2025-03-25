class MetarReport:
    def __init__(self, metar_id, icaoId, receiptTime, obsTime, reportTime, temp, dewp, wdir, wspd, wgst, 
                 visib, altim, slp, qcField, wxString, presTend, maxT, minT, maxT24, minT24, precip, 
                 pcp3hr, pcp6hr, pcp24hr, snow, vertVis, metarType, rawOb, mostRecent, lat, lon, elev, 
                 prior, name, clouds):
        self.metar_id = metar_id
        self.icaoId = icaoId
        self.receiptTime = receiptTime
        self.obsTime = obsTime
        self.reportTime = reportTime
        self.temp = temp
        self.dewp = dewp
        self.wdir = wdir
        self.wspd = wspd
        self.wgst = wgst
        self.visib = visib
        self.altim = altim
        self.slp = slp
        self.qcField = qcField
        self.wxString = wxString
        self.presTend = presTend
        self.maxT = maxT
        self.minT = minT
        self.maxT24 = maxT24
        self.minT24 = minT24
        self.precip = precip
        self.pcp3hr = pcp3hr
        self.pcp6hr = pcp6hr
        self.pcp24hr = pcp24hr
        self.snow = snow
        self.vertVis = vertVis
        self.metarType = metarType
        self.rawOb = rawOb
        self.mostRecent = mostRecent
        self.lat = lat
        self.lon = lon
        self.elev = elev
        self.prior = prior
        self.name = name
        self.clouds = [CloudLayer(**cloud) for cloud in clouds] if clouds else []

    def __repr__(self):
        return f"MetarReport({self.icaoId}, {self.reportTime}, Temp: {self.temp}°C, Wind: {self.wdir}° @ {self.wspd}kt)"

class CloudLayer:
    def __init__(self, cover, base):
        self.cover = cover
        self.base = base

    def __repr__(self):
        return f"CloudLayer({self.cover}, Base: {self.base} ft)"