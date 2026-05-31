def analyze_job_market(industry, region, hiring_rate):

    match industry.lower():

        case "it":
            industry_name = "Information Technology"

        case "healthcare":
            industry_name = "Healthcare"

        case "education":
            industry_name = "Education"

        case "construction":
            industry_name = "Construction"

        case "finance":
            industry_name = "Finance"

        case _:
            industry_name = "Unknown Industry"

    if hiring_rate >= 80:
        demand = "High Demand"

    elif hiring_rate >= 50:
        demand = "Medium Demand"

    else:
        demand = "Low Demand"

    print("Industry:", industry_name)
    print("Demand Level:", demand)
