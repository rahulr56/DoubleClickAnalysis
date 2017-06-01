import time
import string
import random
import hashlib

eventTypes = ["VIEW","CLICK","CONVERSION",""]
eventSubTypes = [ "VIEW" , "CLICK", "POSTVIEW" , "POSTCLICK" ]
dbmViewStates = [ "inner", "outer" ]
advertiserIds = []
commercialIds = []
for i in xrange(1,101):
    seed=int(str(time.time()).split('.')[0])
    advertiserIds.append(seed + random.randint(1,2000))
    commercialIds.append(seed/random.randint(1,200)+10876554)

for i in xrange(100000):
    seed=int(str(time.time()).split('.')[0])
    referralURL = hashlib.sha256(str(random.randint(0,seed))).hexdigest()
    impressionID = hashlib.md5(str(((i-seed)/random.randint(1,200)))).hexdigest()
    eligibleImpressions = random.randint(0,seed)
    measurableImpressions = random.randint(0,seed)
    viewableImpressions = random.randint(0,seed)
    activityId = long(str(measurableImpressions/viewableImpressions*seed*seed*10000).split('.')[0])
    if activityId == 0 :
        activityId = long(str(measurableImpressions/viewableImpressions*seed*seed*10000).split('.')[0])
    eventTime = random.randint(1,200)+seed
    eventType = random.randint(0,3)
    eventSubType = 0 
    dbmViewState = 0 
    dbmAttributedInventorySource = "True"
    if eventType == 3 or eventType == 2:
        if seed % 2 == 0 :
            eventSubType = 3
            dbmViewState = 1 
            dbmAttributedInventorySource = "True"
        else:
            eventSubType = 2
            dbmViewState = 0 
            dbmAttributedInventorySource = "False"
    else:
        eventSubType = random.randint(0,2)
    userId = hashlib.sha256(eventTypes[eventType] + eventSubTypes[eventSubType] + str(seed)).hexdigest()
    advertiserId = advertiserIds[random.randint(0,99)]
    commercialId = commercialIds[random.randint(0,99)]
    adId  = int( (seed * seed) / random.randint(1,87746))
    renderingId  = int( (seed * random.randint(76546,54326457) / random.randint(76775,765643)) )
    creativeVersion = random.randint(1, 65535)
    siteId = random.randint(156635214,7867543234567890)
    placementId = random.randint(156635214,7867543234567890)
    countryCode="".join(random.choice(string.ascii_uppercase) for _ in range(2))
    state ="".join(random.choice(string.ascii_uppercase) for _ in range(2))
    browserPlatformVersion = "".join(random.choice(string.ascii_uppercase + string.digits) for _ in range(20))
    osId = random.randint(7564,778754)
    dmaId = long("".join(random.choice(string.digits) for _ in range(12)))
    cityId  = long("".join(random.choice(string.digits) for _ in range(12)))
    postalCode = "".join(random.choice(string.digits) for _ in range(5))
    uvalue = "".join(random.choice(string.digits + string.ascii_uppercase) for _ in range(20))
    transId = "".join(random.choice(string.digits + string.ascii_uppercase) for _ in range(20))
    otherData = "".join(random.choice(string.digits + string.ascii_uppercase) for _ in range(30))
    ordValue = "".join(random.choice(string.digits + string.ascii_uppercase) for _ in range(20))
    interactionTime = "".join(random.choice(string.digits) for _ in range(10))+ "." + "".join(random.choice(string.digits) for _ in range(6))
    conversionId = int("".join(random.choice(string.digits) for _ in range(20)))
    segmentValue = long("".join(random.choice(string.digits) for _ in range(20)))
    richMediaEvent = long("".join(random.choice(string.digits) for _ in range(20)))
    totalConversion = int("".join(random.choice(string.digits) for _ in range(20)))
    totalRevenue = "".join(random.choice(string.digits) for _ in range(10))+ "." + "".join(random.choice(string.digits) for _ in range(6))
    eventTimer = "".join(random.choice(string.digits) for _ in range(2))+ "." + "".join(random.choice(string.digits) for _ in range(6))
    eventCounter = "".join(random.choice(string.digits) for _ in range(2))+ "." + "".join(random.choice(string.digits) for _ in range(6))
    parner1Id ="".join(random.choice(string.ascii_uppercase) for _ in range(20))
    parner2Id ="".join(random.choice(string.ascii_uppercase) for _ in range(20))
    dbmAuctionId = "".join(random.choice(string.digits + string.ascii_uppercase) for _ in range(20))
    dbmRequestTime = "".join(random.choice(string.digits ) for _ in range(15))
    dbmAdvertiserId = "".join(random.choice(string.digits ) for _ in range(25))
    dbmInserrtionOrderId = "".join(random.choice(string.digits ) for _ in range(10))
    dbmLineItemId = "".join(random.choice(string.digits ) for _ in range(10))
    dbmCreativeId = "".join(random.choice(string.digits ) for _ in range(10))
    dbmBidPriceUSD = "".join(random.choice(string.digits ) for _ in range(10))
    dbmBidPricePartner = "".join(random.choice(string.digits ) for _ in range(10))
    dbmBidPriceAdvertiser = "".join(random.choice(string.digits ) for _ in range(10))
    dbmUrl = "http://"+"".join(random.choice(string.digits + string.ascii_uppercase) for _ in range(20))
    dbmsiteId = "".join(random.choice(string.digits ) for _ in range(10))
    dbmLanguage = "".join(random.choice(string.ascii_lowercase) for _ in range(2)) + "_" +"".join(random.choice(string.ascii_uppercase) for _ in range(3))
    dbmAdxPageCategories=[]
    dbmTargettedKeywords=[]
    for x in range (3):
        dbmAdxPageCategories.append("".join(random.choice(string.digits ) for _ in range(3)))
        dbmTargettedKeywords.append("".join(random.choice(string.ascii_uppercase ) for _ in range(3)))
    dbmAdxPageCategory = " ".join(dbmAdxPageCategories)
    dbmTargettedKeyword = " ".join(dbmTargettedKeywords)
    dbmExcahngeID = "".join(random.choice(string.digits ) for _ in range(10))
    dbmInventorySourceId ="".join(random.choice(string.ascii_uppercase + string.digits) for _ in range(20))
    dbmAdPosition= long("".join(random.choice(string.digits) for _ in range(20)))
    dbmCountryCode = "".join(random.choice(string.ascii_uppercase ) for _ in range(2))
    dbmDesignatedMarketID = "".join(random.choice(string.digits ) for _ in range(3))
    dbmPostalCode = "".join(random.choice(string.digits ) for _ in range(5))
    dbmState = long("".join(random.choice(string.digits ) for _ in range(5)))
    dbmOSId = long("".join(random.choice(string.digits ) for _ in range(5)))
    dbmBrowserId = long("".join(random.choice(string.digits ) for _ in range(5)))
    dbmTimeZone = long("".join(random.choice(string.digits ) for _ in range(5)))
    dbmNetSpeed = long("".join(random.choice(string.digits ) for _ in range(5)))
    dbmMatchingTargettedSystems = ("".join(random.choice(string.digits ) for _ in range(5)))
    dbmISPId = long("".join(random.choice(string.digits ) for _ in range(15)))
    dbmDeviceType = long("".join(random.choice(string.digits ) for _ in range(3)))
    dbmMobileMakeId = long("".join(random.choice(string.digits ) for _ in range(3)))
    dbmMobileModelId = long("".join(random.choice(string.digits ) for _ in range(4)))
    dbmMediaCostPriceUSD = "".join(random.choice(string.digits ) for _ in range(10))
    dbmMediaCostPricePartner = "".join(random.choice(string.digits ) for _ in range(10))
    dbmMediaCostPriceAdvertiser = "".join(random.choice(string.digits ) for _ in range(10))
    dbmMediaRevenueUSD = "".join(random.choice(string.digits ) for _ in range(10))
    dbmMediaRevenuePartner = "".join(random.choice(string.digits ) for _ in range(10))
    dbmMediaRevenueAdvertiser = "".join(random.choice(string.digits ) for _ in range(10))
    dbmTotalPriceUSD = "".join(random.choice(string.digits ) for _ in range(10))
    dbmTotalPricePartner = "".join(random.choice(string.digits ) for _ in range(10))
    dbmTotalPriceAdvertiser = "".join(random.choice(string.digits ) for _ in range(10))
    dbmCPMfee1Usd = "".join(random.choice(string.digits ) for _ in range(10))
    dbmCPMfee1Partner = "".join(random.choice(string.digits ) for _ in range(10))
    dbmCPMfee1Advertiser = "".join(random.choice(string.digits ) for _ in range(10))
    dbmCPMfee2Usd = "".join(random.choice(string.digits ) for _ in range(10))
    dbmCPMfee2Partner = "".join(random.choice(string.digits ) for _ in range(10))
    dbmCPMfee2Advertiser = "".join(random.choice(string.digits ) for _ in range(10))
    dbmCPMfee3Usd = "".join(random.choice(string.digits ) for _ in range(10))
    dbmCPMfee3Partner = "".join(random.choice(string.digits ) for _ in range(10))
    dbmCPMfee3Advertiser = "".join(random.choice(string.digits ) for _ in range(10))
    dbmCPMfee4Usd = "".join(random.choice(string.digits ) for _ in range(10))
    dbmCPMfee4Partner = "".join(random.choice(string.digits ) for _ in range(10))
    dbmCPMfee4Advertiser = "".join(random.choice(string.digits ) for _ in range(10))
    dbmCPMfee5Usd = "".join(random.choice(string.digits ) for _ in range(10))
    dbmCPMfee5Partner = "".join(random.choice(string.digits ) for _ in range(10))
    dbmCPMfee5Advertiser = "".join(random.choice(string.digits ) for _ in range(10))
    dbmMediafee1Usd = "".join(random.choice(string.digits ) for _ in range(10))
    dbmMediafee1Partner = "".join(random.choice(string.digits ) for _ in range(10))
    dbmMediafee1Advertiser = "".join(random.choice(string.digits ) for _ in range(10))
    dbmMediafee2Usd = "".join(random.choice(string.digits ) for _ in range(10))
    dbmMediafee2Partner = "".join(random.choice(string.digits ) for _ in range(10))
    dbmMediafee2Advertiser = "".join(random.choice(string.digits ) for _ in range(10))
    dbmMediafee3Usd = "".join(random.choice(string.digits ) for _ in range(10))
    dbmMediafee3Partner = "".join(random.choice(string.digits ) for _ in range(10))
    dbmMediafee3Advertiser = "".join(random.choice(string.digits ) for _ in range(10))
    dbmMediafee4Usd = "".join(random.choice(string.digits ) for _ in range(10))
    dbmMediafee4Partner = "".join(random.choice(string.digits ) for _ in range(10))
    dbmMediafee4Advertiser = "".join(random.choice(string.digits ) for _ in range(10))
    dbmMediafee5Usd = "".join(random.choice(string.digits ) for _ in range(10))
    dbmMediafee5Partner = "".join(random.choice(string.digits ) for _ in range(10))
    dbmMediafee5Advertiser = "".join(random.choice(string.digits ) for _ in range(10))
    dbmDataFeeUSD = "".join(random.choice(string.digits ) for _ in range(10))
    dbmDatafeePartner = "".join(random.choice(string.digits ) for _ in range(10))
    dbmDatafeeAdvertiser = "".join(random.choice(string.digits ) for _ in range(10))
    dbmBillableCostUSD = "".join(random.choice(string.digits ) for _ in range(10))
    dbmBillableCostPartner = "".join(random.choice(string.digits ) for _ in range(10))
    dbmBillableCostAdvertiser = "".join(random.choice(string.digits ) for _ in range(10))

    print  referralURL + "," + str(impressionID) + "," + str(eligibleImpressions) + "," + str(measurableImpressions) + "," + str(viewableImpressions) + "," + str(activityId) + "," + str(eventTime) + "," + str(eventType) + "," + str(eventSubType) + "," + str(userId) + "," + str(advertiserId) + "," + str(commercialId) + "," + str(adId) + "," + str(renderingId) + "," + str(creativeVersion) + "," + str(siteId) + "," + str(placementId) + "," + str(countryCode) + "," + str(state) + "," + str(browserPlatformVersion) + "," + str(osId) + "," + str(dmaId) + "," + str(cityId) + "," + str(postalCode) + "," + str(uvalue) + "," + str(transId) + "," + str(otherData) + "," + str(ordValue) + "," + str(interactionTime) + "," + str(conversionId) + "," + str(segmentValue) + "," + str(richMediaEvent) + "," + str(totalConversion) + "," + str(totalRevenue) + "," + str(eventTimer) + "," + str(eventCounter) + "," + str(parner1Id) + "," + str(parner2Id) + "," + str(dbmViewState) + "," + str(dbmAuctionId) + "," + str(dbmRequestTime) + "," + str(dbmAdvertiserId) + "," + str(dbmInserrtionOrderId) + "," + str(dbmLineItemId) + "," + str(dbmCreativeId) + "," + str(dbmBidPriceUSD) + "," + str(dbmBidPricePartner) + "," + str(dbmBidPriceAdvertiser) + "," + str(dbmUrl) + "," + str(dbmsiteId) + "," + str(dbmLanguage) + "," + str(dbmAdxPageCategories) + "," + str(dbmTargettedKeywords) + "," + str(dbmExcahngeID) + "," + str(dbmAttributedInventorySource) + "," + str(dbmInventorySourceId) + "," + str(dbmAdPosition) + "," + str(dbmCountryCode) + "," + str(dbmDesignatedMarketID) + "," + str(dbmPostalCode) + "," + str(dbmState) + "," + str(dbmOSId) + "," + str(dbmBrowserId) + "," + str(dbmTimeZone) + "," + str(dbmNetSpeed) + "," + str(dbmMatchingTargettedSystems) + "," + str(dbmISPId) + "," + str(dbmDeviceType) + "," + str(dbmMobileMakeId) + "," + str(dbmMobileModelId) + "," + str(dbmMediaCostPriceUSD) + "," + str(dbmMediaCostPricePartner) + "," + str(dbmMediaCostPriceAdvertiser) + "," + str(dbmMediaRevenueUSD) + "," + str(dbmMediaRevenuePartner) + "," + str(dbmMediaRevenueAdvertiser) + "," + str(dbmTotalPriceUSD) + "," + str(dbmTotalPricePartner) + "," + str(dbmTotalPriceAdvertiser) + "," + str(dbmCPMfee1Usd) + "," + str(dbmCPMfee1Partner) + "," + str(dbmCPMfee1Advertiser) + "," + str(dbmCPMfee2Usd) + "," + str(dbmCPMfee2Partner) + "," + str(dbmCPMfee2Advertiser) + "," + str(dbmCPMfee3Usd) + "," + str(dbmCPMfee3Partner) + "," + str(dbmCPMfee3Advertiser) + "," + str(dbmCPMfee4Usd) + "," + str(dbmCPMfee4Partner) + "," + str(dbmCPMfee4Advertiser) + "," + str(dbmCPMfee5Usd) + "," + str(dbmCPMfee5Partner) + "," + str(dbmCPMfee5Advertiser) + "," + str(dbmMediafee1Usd) + "," + str(dbmMediafee1Partner) + "," + str(dbmMediafee1Advertiser) + "," + str(dbmMediafee2Usd) + "," + str(dbmMediafee2Partner) + "," + str(dbmMediafee2Advertiser) + "," + str(dbmMediafee3Usd) + "," + str(dbmMediafee3Partner) + "," + str(dbmMediafee3Advertiser) + "," + str(dbmMediafee4Usd) + "," + str(dbmMediafee4Partner) + "," + str(dbmMediafee4Advertiser) + "," + str(dbmMediafee5Usd) + "," + str(dbmMediafee5Partner) + "," + str(dbmMediafee5Advertiser) + "," + str(dbmDataFeeUSD) + "," + str(dbmDatafeePartner) + "," + str(dbmDatafeeAdvertiser) + "," + str(dbmBillableCostUSD) + "," + str(dbmBillableCostPartner) + "," + str(dbmBillableCostAdvertiser)
