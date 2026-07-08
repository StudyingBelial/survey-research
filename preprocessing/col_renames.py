cols_to_positional_extract = {
    55: "rank_most_important_factors_when_building_ai",
    68: "rank_ethical_priorities_in_country",
}

cols_to_parse = {
    25: "ai_powered_tools_used",
    34: "benefit_of_ai_to_country",
    35: "concerns_about_ai_use_in_country",
    39: "applications_thought_to_use_ai",
}

col_one_hot = {
    4: "gender",
    5: "age_range",
    6: "marital_status",
    7: "highest_education",
    8: "ethnicity",
    10: "residence_country",
    11: "residence_type",
}

col_binary = {
    15: "formal_ai_education",
    17: "works_with_ai",
    23: "aware_of_national_ai_programs",
    24: "used_ai_product",
    26: "ai_in_agriculture",
    27: "ai_in_healthcare",
    28: "ai_in_education",
    29: "ai_in_tourism",
    30: "ai_in_disaster_management",
    31: "ai_in_public_services",
    36: "directly_affected_by_ai",
    38: "aware_ai_can_be_wrong",
    81: "interested_in_ai_course",
}

col_ordinal = {
    14: "internet_usage_frequency",
    16: "daily_ai_exposure",
    18: "computer_proficiency",
    19: "ai_familiarity",
    20: "confidence_understanding_ai",
    21: "general_feeling_about_ai",
    22: "future_ai_impact",

    32: "current_ai_impact_on_daily_life",
    33: "awareness_of_ai_usage",

    40: "trust_ai_healthcare",
    41: "trust_ai_insurance",
    42: "trust_ai_agriculture",
    43: "trust_ai_finance",
    44: "trust_ai_military",
    45: "trust_ai_law_enforcement",
    46: "trust_ai_environment",
    47: "trust_ai_education",
    48: "trust_ai_transportation",
    49: "trust_ai_manufacturing",
    50: "trust_ai_human_resources",
    51: "trust_ai_remittance",

    52: "accept_ai_hiring",
    53: "accept_ai_energy_meter",

    37: "have_government_policy_to_guide_ai_development",
    
    56: "support_national_ai_laws",
    57: "support_voluntary_ai_certification",
    58: "support_independent_ai_monitoring",
    59: "support_company_self_regulation",
    60: "support_ai_transparency",
    61: "support_diverse_ai_development",

    62: "trust_national_government",
    63: "trust_international_bodies",
    64: "trust_universities",
    65: "trust_consumer_groups",
    66: "trust_tech_companies",
    67: "trust_social_media_companies",

    69: "support_national_ai_policies",
    70: "support_ai_local_language_education",
    71: "support_public_private_partnerships",
    72: "support_rural_internet",
    73: "support_ai_literacy",

    74: "trust_national_government_to_lead_ai",
    75: "trust_local_tech_companies_to_lead_ai",
    76: "trust_international_ngos_to_lead_ai",
    77: "trust_academic_institutions_to_lead_ai",
    78: "trust_cooperative_societies_to_lead_ai",

    79: "trust_domestic_ai_more",
    80: "perceived_ai_impact_after_survey",
}

col_ignore = {
    0: "row_id",
    1: "id",
    2: "start_time",
    3: "completion_time",
    54: "ranking_instruction_only",
    82: "hash_id",
}