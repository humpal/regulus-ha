# registry_mapper_ir14_1_0_10_6.py

REGISTRY_MAPPER = {

    # ==========================================
    # AKU
    # ==========================================

    "akuState": "__R19406.0_BOOL_i",
    "akuComfortTemperature": "__R19407_USINT_u",
    "akuSetbackTemperature": "__R19408_USINT_u",

    # ==========================================
    # HOT WATER
    # ==========================================

    "waterState": "__R24792.0_BOOL_i",
    "waterComfortTemperature": "__R24812_REAL_.0f",
    "waterSetbackTemperature": "__R24816_USINT_u",
    "waterSwitchingSensorTemperature": "__R8327_REAL_.1f",
    "waterRequiredTemperature": "__R8505_INT_d",
    "waterAdHocTriggerState": "__R24829.0_BOOL_i",
    "waterAdHocTriggerRequiredTemperature": "__R24828_SINT_d",

    # ==========================================
    # DASHBOARD & SYSTÉM
    # ==========================================
    "outdoorTemperature": "__R8267_REAL_.1f",
    "rcTariff": "__R11097.2_BOOL_i",
    "holiday": "__R8266.1_BOOL_i",
    "heatPumpRunningStatus": "__R28749.2_BOOL_i",          # TČ 1 running bit (compressor active)
    "heatPumpOutletTemperature": "__R28433_INT_-5.1d",     # Fixed format: -5.1d (was -4.1d)
    "heatPumpInletTemperature": "__R28429_INT_-5.1d",      # Fixed format: -5.1d (was -4.1d)
    "waterRunningStatusFromHeatPump": "__R24792.0_BOOL_i",
    "circulationRunningStatus": "__R11097.0_BOOL_i",

    # === Zóna 4: Chlazení dům ===
    "zone4State": "__R16970.0_BOOL_i",
    "zone4Temperature": "__R132076_REAL_.1f",
    "zone4DesiredTemperature": "__R122618_REAL_.1f",

    # === Zóna 5: Chlazení spíž ===
    "zone5State": "__R17360.0_BOOL_i",
    "zone5CoolingState": "__R17569.1_BOOL_i",
    "zone5Temperature": "__R132098_REAL_.1f",
    "zone5DesiredTemperature": "__R17362_REAL_.1f",
    "zone5Humidity": "__R132106_REAL_.1f",
    "zone5HeatingWaterTemperature": "__R8343_REAL_.1f",
    "zone5RequiredHeatingWaterTemperature": "__R8445_REAL_.1f",

    # === Zóna 6: Bazén ===
    "zone6State": "__R17750.0_BOOL_i",
    "zone6Temperature": "__R132120_REAL_.1f",
    "zone6DesiredTemperature": "__R129038_REAL_.1f",

    # === UNI 2 chlazeni ===
    "uni2State": "__R24458.1_BOOL_i",
    "uni2Temperature": "__R9706_REAL_.1f",
    "uni2DesiredTemperature": "__R24477_REAL_.1f",
    "uni2TriggerOnDiff": "__R24482_REAL_.1f",
    "uni2TriggerOffDiff": "__R24486_REAL_.1f",

    # ==========================================
    # DONE
    # ==========================================

    # ==========================================
    # ZÓNY (Očekávaný formát z verze 1.0.10.0)
    # ==========================================

    # === Zóna 1: Podlahovka ===
    "zone1RunningStatus": "__R16492_USINT_u",  # Status běhu zóny 1
    "zone1RequiredTemperature": "__R8453_REAL_.1f",  # Vypočtená žádaná teplota zóny 1
    "zone1HeatingWaterTemperature": "__R8323_REAL_.1f",  # Aktuální teplota zóny 1
    "zone1RequiredHeatingWaterTemperature": "__R8429_REAL_.1f",  # Požadovaná teplota otopné vody
    "zone1SummerMode": "__R16394.0_BOOL_i",  # Letní režim zóny 1 (odhad dle offsetu)

    # === Zóna 2: Koupelny Žebřík ===
    "zone2RunningStatus": "__R19754_USINT_u",  # Status běhu zóny 2
    "zone2Temperature": "__R8331_REAL_.1f",  # (Specifikum z 10.0 mapperu - teplota)
    "zone2RequiredTemperature": "__R8457_REAL_.1f",  # Vypočtená žádaná teplota zóny 2
    "zone2HeatingWaterTemperature": "__R8331_REAL_.1f",  # Aktuální teplota zóny 2
    "zone2RequiredHeatingWaterTemperature": "__R8433_REAL_.1f",  # Požadovaná teplota otopné vody
    "zone2SummerMode": "__R19656.0_BOOL_i",  # Letní režim zóny 2

    # === Zóna 3: Topení ===
    "zone3RunningStatus": "__R16882_USINT_u",
    "zone3RequiredTemperature": "__R8461_REAL_.1f",
    "zone3HeatingWaterTemperature": "__R8335_REAL_.1f",
    "zone3RequiredHeatingWaterTemperature": "__R8437_REAL_.1f",



    # ==========================================
    # HEAT PUMP
    # ==========================================
    "hpIdleTime": "__R29003_TIME_Thh:mm:ss",
    "hpRunningTime": "__R28991_TIME_Thh:mm:ss",
    "hpMasterSwitch": "__R28749.0_BOOL_i",          # TČ 1 master on/off switch
    "hpCompressorRunning": "__R28749.2_BOOL_i",      # TČ 1 compressor active bit
    "hpStatusText": "__R26408_STRING[20]_s",         # STAV TČ: text (e.g. "topí")
    "hpCompressorSpeed": "__R28665_INT_-5.1d",       # Compressor speed (ot/s)

    # ==========================================
    # AKU & VODA (TV)
    # ==========================================
    "akuTopTemperature": "__R8275_REAL_.1f",  # AKU aktuální teplota
    "akuBottomTemperature": "__R8275_REAL_.1f",  # AKU aktuální teplota (pokud je 1 čidlo)
    "akuRequiredTemperature": "__R108006_REAL_.1f",  # AKU požadovaná

    # ==========================================
    # STATISTIKY TČ A VODY (verified from zd_t.xml snapshot, firmware 1.0.10.6)
    # ==========================================
    "overallTotalHours": "__R28965_UDINT_u",
    "overallTotalStarts": "__R28975_UINT_u",
    "overallTodayHours": "__R28937_USINT_u",
    "overallTodayMinutes": "__R28938_UINT_u",
    "overallTodayStarts": "__R28977_USINT_u",
    "overallYesterdayHours": "__R28959_USINT_u",
    "overallYesterdayMinutes": "__R28960_UINT_u",
    "overallYesterdayStarts": "__R28978_USINT_u",
    "hotWaterTotalHours": "__R28969_UDINT_u",
    "hotWaterTotalStarts": "__R28979_UINT_u",
    "hotWaterTodayHours": "__R28944_USINT_u",
    "hotWaterTodayMinutes": "__R28945_UINT_u",
    "hotWaterTodayStarts": "__R28981_USINT_u",
    "hotWaterYesterdayHours": "__R28962_USINT_u",
    "hotWaterYesterdayMinutes": "__R28963_UINT_u",
    "hotWaterYesterdayStarts": "__R28982_USINT_u",

    # ==========================================
    # SERVISNÍ SPECIALITY (Tvé vlastní klíče)
    # ==========================================
    "heatPumpTriggerOnDifference": "__R24786_SINT_d",  # Diference pro zapnutí TČ
    "heatPumpTriggerOffHysteresis": "__R24787_SINT_d",  # Diference pro vypnutí TČ
    "heatPumpPassiveCooling": "__R24785.2_BOOL_i",  # Pasivní chlazení toggle
    "hotWaterTriggerOnDifference": "__R24804_REAL_.0f",  # Diference pro zapnutí TUV
}