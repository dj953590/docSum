class Queries:
    def __init__(self, symbol):
        self.symbol = symbol
        self.queries = {
            "Overview": f"""
    Based on the comprehensive review of the latest 10-K filing of {self.symbol}, identify and analyze three positive and three negative aspects regarding the company's prospects. Organize your analysis in the following format:

    1. **Positive Insights**:
        - **Strengths and Opportunities**: Detail three major strengths or opportunities that {self.symbol} is poised to capitalize on.
        - **Potential Positive Outcomes**: Discuss the possible beneficial outcomes if these strengths and opportunities are effectively leveraged.

    2. **Negative Insights**:
        - **Challenges and Threats**: Enumerate three significant challenges or threats facing {self.symbol}.
        - **Potential Negative Consequences**: Explore the potential adverse impacts these challenges could have on {self.symbol}'s future performance.
    """,
            "Business and Risk": f"""
    Using the combined information from Item 1 (Business Overview), Item 1A (Risk Factors), Item 7 (Management’s Discussion and Analysis), Item 7A (Quantitative and Qualitative Disclosures About Market Risk), and Item 8 (Financial Statements) from the latest 10-K filing of {self.symbol}, perform a detailed analysis to provide:

    1. **Business and Financial Overview**:
        - **Core Business Operations**: Summarize the main activities and market positions outlined in Item 1.
        - **Financial Health**: From Item 8, highlight key financial metrics and year-over-year changes.
        - **Management Analysis**: Extract key insights from Item 7 about financial trends, operational challenges, and management's strategic focus.

    2. **Integrated Risk Profile**:
        - **Risk Landscape**: Using information from Item 1A and Item 7A, identify and describe the major operational and market risks.
        - **Impact and Mitigation**: Discuss the potential impacts of these risks on the business and financial performance, and outline the risk mitigation strategies provided by management across these sections.

    Provide this analysis in a structured format, aiming to offer stakeholders a clear and concise overview of both opportunities and threats, as well as the company’s preparedness to handle its market and operational challenges.
    """,
            "Strategic Outlook and Future Projections": f"""
    With reference to the information available in Item 1 (Business Overview), Item 1A (Risk Factors), Item 7 (Management’s Discussion and Analysis), Item 7A (Quantitative and Qualitative Disclosures About Market Risk), and Item 8 (Financial Statements) of {self.symbol}'s recent 10-K filing, synthesize a strategic report that addresses:

    1. **Strategic Positioning and Opportunities**:
        - **Market Dynamics**: Analyze the business landscape as described in Item 1 and Item 7, focusing on competitive positioning and market opportunities.
        - **Operational Strengths**: Highlight operational strengths and efficiencies that bolster the company's market position.

    2. **Future Financial Prospects**:
        - **Financial Projections**: Discuss future financial prospects based on trends and data from Item 7 and Item 8.
        - **Risk and Opportunities Balance**: Weigh the financial risks (Item 1A and 7A) against potential opportunities, and discuss how the company plans to leverage its strengths to mitigate these risks and capitalize on market trends.

    This analysis should offer a forward-looking perspective, aiming to provide potential investors and company stakeholders with a deep understanding of the company’s strategic initiatives, market risks, and financial outlook.
"""
        }

    def get_query(self, query_name):
        return self.queries.get(query_name)
