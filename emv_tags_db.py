import interpritators

tags = ([ "TAG_TERMINAL_VERIFICATION_RESULTS", "95",   { "Name" : "TVR",  "Description" : "Terminal Verification results","Value":"0000000000" ,"Interpritator":interpritators.tvr_inter}],
[ "TAG_TERMINAL_VERIFICATION_RESULTS_2"      , "0095", { "Name" : "TVR",  "Description" : "Terminal Verification results","Value":"0000000000" ,"Interpritator":interpritators.tvr_inter }],
[ "TAG_TERMINAL_CAPABILITIES"                , "9F33", { "Name" : "Terminal capabilities", "Description" : "Terminal capabilities","Value":"000000" ,"Interpritator":interpritators.term_cap_inter}],
[ "TAG_AIP"                                  , "82",   { "Name" : "Application interchange profile","Description" : "Application interchange profile", "Value":"0000","Interpritator":interpritators.aip_inter}],
[ "TAG_TSI"                                  , "9B",   { "Name" : "Transaction status information", "Description" : "Transaction status information","Value":"0000","Interpritator":interpritators.tsi_inter}],
[ "TAG_AUTHORISATION_RESPONSE_CODE"          , "8A",   { "Name" : "Auth resp code", "Description" : "Auth resp code","Value":"00" ,"Interpritator":interpritators.resp_code_inter}],
[ "TAG_ADDITIONAL_TERMINAL_CAPABILITIES"     , "9F40", { "Name" : "Additional terminal capabilities", "Description" : "Additional terminal capabilities","Value":"0000000000","Interpritator":interpritators.add_term_cap_inter}],
[ "TAG_TERMINAL_TRANSACTION_QUALIFIERS"      , "9F66", { "Name" : "Terminal Transaction Qualifiers", "Description" : "Is a reader data element indicating capabilities (e.g., MSD or qVSDC) and transaction-specific requirements (e.g., online) of the reader.","Value":"0000000000","Interpritator":interpritators.ttq_inter}],
[ "TAG_IAC_DEFAULT"                          , "9F0D", { "Name" : "Action Code Default","Description" : "Action Code Default","Value":"0000000000","Interpritator":interpritators.tacdef_inter}],
[ "TAG_IAC_DENIAL"                           , "9F0E", { "Name" : "Action Code Denial","Description" : "Action Code Denial","Value":"0000000000","Interpritator":interpritators.tacden_inter}],
[ "TAG_IAC_ONLINE"                           , "9F0F", { "Name" : "Action Code Online","Description" : "Action Code Online","Value":"0000000000","Interpritator":interpritators.taconl_inter}],
[ "TAG_AMOUNT_AUTHORISED"                             , "9F02"],
[ "TAG_FCI_ISSUER_DISCRETIONARY_DATA"                 , "BF0C"],
[ "TAG_AMOUNT_AUTHORISED_BINARY"                      , "81"],
[ "TAG_AMOUNT_AUTHORISED_BINARY_2"                    , "0081"],
[ "TAG_AMOUNT_OTHER"                                  , "9F3"],
[ "TAG_APPLICATION_CONTROL"                           , "C1"],
[ "TAG_APPLICATION_CONTROL_2"                         , "00C1"],
[ "TAG_APPLICATION_CRYPTOGRAM"                        , "9F26"],
[ "TAG_APPLICATION_CURRENCY_CODE"                     , "9F42"],
[ "TAG_APPLICATION_CURRENCY_EXPONENT"                 , "9F44"],
[ "TAG_APPLICATION_DISCRETIONARY_DATA"                , "9F05"],
[ "TAG_APPLICATION_EFFECTIVE_DATE"                    , "5F25"],
[ "TAG_APPLICATION_EXPIRATION_DATE"                   , "5F24"],
[ "TAG_APPLICATION_FILE_LOCATOR"                      , "94"],
[ "TAG_APPLICATION_FILE_LOCATOR_2"                    , "0094"],
[ "TAG_APPLICATION_IDENTIFIER"                        , "4F"],
[ "TAG_APPLICATION_IDENTIFIER_2"                      , "004F"],
[ "TAG_AID"                                           , "9F06"],
[ "TAG_AIP_2"                                         , "0082"],
[ "TAG_APPLICATION_ISSUER_LIFE_CYCLE_DATA"            , "C8"],
[ "TAG_APPLICATION_ISSUER_LIFE_CYCLE_DATA_2"          , "00C8"],
[ "TAG_APPLICATION_LABEL"                             , "50"],
[ "TAG_APPLICATION_LABEL_2"                           , "0050"],
[ "TAG_APPLICATION_LIFE_CYCLE_DATA"                   , "9F7E"],
[ "TAG_APPLICATION_PAN"                               , "5A"],
[ "TAG_APPLICATION_PAN_2"                             , "005A"],
[ "TAG_APPLICATION_PREFERRED_NAME"                    , "9F12"],
[ "TAG_APPLICATION_PRIORITY_INDICATOR"                , "87"],
[ "TAG_APPLICATION_PRIORITY_INDICATOR_2"              , "0087"],
[ "TAG_ATC"                                           , "9F36"],
[ "TAG_AUC"                                           , "9F07"],
[ "TAG_APPLICATION_VERSION_NUMBER "                   , "9F08"],
[ "TAG_AUTHORISATION_RESPONSE_CODE_2"                 , "008A"],
[ "TAG_BANK_IDENTIFIER_CODE"                          , "5F54"],
[ "TAG_CDOL1"                                         , "8C"],
[ "TAG_CDOL1_2"                                       , "008C"],
[ "TAG_CDOL2"                                         , "8D"],
[ "TAG_CDOL2_2"                                       , "008D"],
[ "TAG_CARD_TRANSACTION_INFORMATION"                 , "9F63"],
[ "TAG_CVR"                                           , "9F52"],
[ "TAG_CARDHOLDER_NAME"                               , "5F20"],
[ "TAG_CARDHOLDER_NAME_EXTENDED"                      , "5F20"],
[ "TAG_CVM_LIST"                                      , "8E"],
[ "TAG_CVM_LIST_2"                                    , "008E"],
[ "TAG_CVM_RESULTS"                                   , "9F34"],
[ "TAG_CA_PUBLIC_KEY_INDEX"                           , "8F"],
[ "TAG_CA_PUBLIC_KEY_INDEX_2"                         , "008F"],
[ "TAG_CID"                                           , "9F27"],
[ "TAG_DAC"                                           , "9F45"],
[ "TAG_DDOL"                                          , "9F49"],
[ "TAG_DFNAME"                                        , "84"],
[ "TAG_DFNAME_2"                                      , "0084"],
[ "TAG_ICC_DYNAMIC_NUMBER"                            , "9F4C"],
[ "TAG_ICC_PIN_ENCHIPHERMENT_PUBLIC_KEY_CERTIFICATE"  , "9F2D"],
[ "TAG_ICC_PIN_ENCHIPHERMENT_PUBLIC_KEY_EXPONENT"     , "9F2E"],
[ "TAG_ICC_PIN_ENCHIPHERMENT_PUBLIC_KEY_REMAINDER"    , "9F2F"],
[ "TAG_ICC_PUBLICKEY_CERTIFICATE"                     , "9F46"],
[ "TAG_ICC_PUBLICKEY_EXPONENT"                        , "9F47"],
[ "TAG_ICC_PUBLICKEY_REMAINDER"                       , "9F48"],
[ "TAG_ISSUER_APPLICATION_DATA"                       , "9F10"],
[ "TAG_ISSUER_AUTHENTICATION_DATA"                    , "91"],
[ "TAG_ISSUER_AUTHENTICATION_DATA_2"                  , "0091"],
[ "TAG_ISSUER_CODE_TABLE_INDEX"                       , "9F11"],
[ "TAG_ISSUER_COUNTRY_CODE"                           , "5F28"],
[ "TAG_ISSUER_COUNTRY_CODE_ALPHA2"                    , "5F55"],
[ "TAG_ISSUER_COUNTRY_CODE_ALPHA3"                    , "5F56"],
[ "TAG_ISSUER_IDENTIFICATION_NUMBER"                  , "42"],
[ "TAG_ISSUER_IDENTIFICATION_NUMBER_2"                , "0042"],
[ "TAG_ISSUER_PUBLICKEY_CERTIFICATE"                  , "90"],
[ "TAG_ISSUER_PUBLICKEY_CERTIFICATE_2"                , "0090"],
[ "TAG_ISSUER_PUBLICKEY_EXPONENT"                     , "9F32"],
[ "TAG_ISSUER_PUBLICKEY_REMAINDER"                    , "92"],
[ "TAG_ISSUER_PUBLICKEY_REMAINDER_2"                  , "0092"],
[ "TAG_ISSUER_URL"                                    , "5F50"],
[ "TAG_LANGUAGE_PREFERENCE"                           , "5F2D"],
[ "TAG_LAST_ONLINE_ATC"                               , "9F13"],
[ "TAG_LOG_ENTRY"                                    , "9F4D"],
[ "TAG_LOG_FORMAT"                                    , "9F4F"],
[ "TAG_LOWER_CONSECUTIVE_OFFLINE_LIMIT"               , "9F14"],
[ "TAG_NUMBER_OF_DAYS_OFFLINE_LIMIT"               , "C3"],
[ "TAG_NUMBER_OF_DAYS_OFFLINE_LIMIT_2"                , "00C3"],
[ "TAG_OFFLINE_BALANCE_CURRENCY_CODE"                 , "C9"],
[ "TAG_OFFLINE_BALANCE_CURRENCY_CODE_2"               , "00C9"],
[ "TAG_OFFLINE_BALANCE"                               , "9F50"],
[ "TAG_PAN_SEQUENCE_NUMBER"                      , "5F34"],
[ "TAG_PDOL"                         , "9F38"],
[ "TAG_POS_ENTRY_MODE"                                , "9F39"],
[ "TAG_PIN_TRY_COUNTER"                               , "9F17"],
[ "TAG_PIN_TRY_LIMIT"                                 , "C6"],
[ "TAG_PIN_TRY_LIMIT_2"                               , "00C6"],
[ "TAG_PTH"                                           , "C7"],
[ "TAG_PTH_2"                                         , "00C7"],
[ "TAG_PROFILE_SELECTION_FILE_ENTRY"                  , "C2"],
[ "TAG_PROFILE_SELECTION_FILE_ENTRY_2"                , "00C2"],
[ "TAG_SDA_TAG_LIST"                                  , "9F4A"],
[ "TAG_SECURITY_LIMITS"                               , "C5"],
[ "TAG_SECURITY_LIMITS_2"                             , "00C5"],
[ "TAG_SECURITY_LIMITS_STATUS"                        , "C4"],
[ "TAG_SECURITY_LIMITS_STATUS_2"                      , "00C4"],
[ "TAG_SERVICE_CODE"                                  , "5F30"],
[ "TAG_SFI"                                        , "88"],
[ "TAG_SDDA"                                          , "9F4B"],
[ "TAG_SSAD"                                          , "93"],
[ "TAG_SSAD_2"                                        , "0093"],
[ "TAG_TERMINAL_COUNTRY_CODE"                         , "9F1A"],
[ "TAG_TERMINAL_TYPE"                                 , "9F35"],
[ "TAG_TDOL"                                          , "97"],
[ "TAG_TDOL_2"                                        , "0097"],
[ "TAG_TRACK1_DISCRETIONARY_DATA"                     , "9F1F"],
[ "TAG_TRACK2_DISCRETIONARY_DATA"                     , "9F20"],
[ "TAG_TRACK2_EQUIVALENT_DATA"                        , "57"],
[ "TAG_TRACK2_EQUIVALENT_DATA_2"                      , "0057"],
[ "TAG_TRANSACTION_CURRENCY_CODE"                     , "5F2A"],
[ "TAG_TRANSACTION_DATE"                              , "9A"],
[ "TAG_TRANSACTION_DATE_2"                            , "009A"],
[ "TAG_TRANSACTION_TIME"                              , "9F21"],
[ "TAG_TRANSACTION_TYPE"                              , "9C"],
[ "TAG_TRANSACTION_TYPE_2"                            , "009C"],
[ "TAG_UNPREDICTABLE_NUMBER"                          , "9F37"],
[ "TAG_UNPREDICTABLE_NUMBER2"                         , "9F7F"],
[ "TAG_Slot_Availability"                             , "9F5F"],
[ "TAG_DS_Summary_1"                                  , "9F7D"],
[ "TAG_UPPER_CONSECUTIVE_OFFLINE_LIMIT"               , "9F23"],
[ "TAG_CONTACTLESS_APPLICATION_CAPABILITIES_TYPE"     , "9F28"],
[ "TAG_MOBILE_CVM_RESULTS"                            , "9F71"],
[ "TAG_FCI_PROPRIETARY_TEMPLATE"                      , "A5"],
[ "TAG_FCI_PROPRIETARY_TEMPLATE_2"                    , "00A5"],
[ "TAG_COMMAND_TEMPLATE"                              , "83"],
[ "TAG_COMMAND_TEMPLATE_2"                            , "0083"],
[ "TAG_FCI_TEMPLATE"                                  , "6F"],
[ "TAG_FCI_TEMPLATE_2"                                , "006F"],
[ "TAG_RECORD_TEMPLATE"                               , "70"],
[ "TAG_RECORD_TEMPLATE_2"                             , "0070"],
[ "TAG_RESPONSE_MESSAGE_TEMPLATE_FORMAT1"             , "80"],
[ "TAG_RESPONSE_MESSAGE_TEMPLATE_FORMAT1_2"           , "0080"],
[ "TAG_RESPONSE_MESSAGE_TEMPLATE_FORMAT2"             , "77"],
[ "TAG_RESPONSE_MESSAGE_TEMPLATE_FORMAT2_2"           , "0077"],
[ "TAG_TRACK1DATA_PAYPASS"                            , "56"],
[ "TAG_TRACK2DATA_PAYPASS"                            , "9F6B"])

#[ TAG_EP_TERMINAL_TRANSACTION_QUALIFIERS            
#[ TAG_EXPRESSPAY_TERMINAL_TRANSACTION_CAPABILITIES
#T,G_TERMINAL_RISK_MANAGMENT_DATA,

#data = [{ "Name" : "TVR",  "Description" : "Terminal Verification results", "Interpritator":0 }]#tvr_inter },
#{"Tag":TAG_TERMINAL_CAPABILITIES,            "Name" : "Terminal capabilities",          "Description" : "Terminal capabilities", "Interpritator":termCap_inter},
#{"Tag":TAG_AIP,                              "Name" : "Application "interchange" profile","Description" : "Application "interchange" profile", "Interpritator":aip_inter},
#{"Tag":TAG_AIP_2",                            "Name" : "Application "interchange profile","Description" : "Application "interchange profile", "Interpritator":aip_inter},
#{"Tag":TAG_AUTHORISATION_RESPONSE_CODE,      "Name" : "Auth resp code",                 "Description" : "Auth resp code", "Interpritator":respCode_inter},
#{"Tag":TAG_AUTHORISATION_RESPONSE_CODE_2",    "Name" : "Auth resp code",                 "Description" : "Auth resp code", "Interpritator":respCode_inter},
#{"Tag":TAG_CVR,                              "Name" : "Card Verification Results",      "Description" : "CVR",  "Interpritator":cvr_inter},
#{"Tag":TAG_IAC_DEFAULT,                      "Name" : "Action Code Default",            "Description" : "Action Code Default","Interpritator":action_codes_inter},
#{"Tag":TAG_IAC_DENIAL,                       "Name" : "Action Code Denial",             "Description" : "Action Code Denial","Interpritator":action_codes_inter},
#{"Tag":TAG_IAC_ONLINE,                       "Name" : "Action Code Online",             "Description" : "Action Code Online","Interpritator":iaction_codes_inter},
#{"Tag":TAG_TSI,                              "Name" : "Transaction status information", "Description" : "Transaction status information","Interpritator":tsi_inter},
#{"Tag":TAG_ADDITIONAL_TERMINAL_CAPABILITIES, "Name" : "Additional terminal capabilities", "Description" : "Additional terminal capabilities","Interpritator":add_term_cap_inter}]
#{"Tag":TAG_TRACK2_EQUIVALENT_DATA }
#{"Tag":TAG_TRACK2_EQUIVALENT_DATA_2"}
#{"Tag":TAG_TRACK1_DISCRETIONARY_DATA}
#{"Tag":TAG_ISSUER_AUTHENTICATION_DATA,}
#{"Tag":TAG_ISSUER_AUTHENTICATION_DATA_1,}"""
#{"Tag":TAG_EP_TERMINAL_TRANSACTION_QUALIFIERS,}