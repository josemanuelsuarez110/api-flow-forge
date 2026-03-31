# Portfolio Case Study: API Flow Forge

## OverView
The **API Flow Forge** is an automated ETL pipeline that bridges the gap between raw external data and actionable business intelligence. Built to handle e-commerce inventory data, it validates the engineering workflow required for modern data-driven applications.

## Technical Stack
- **Languages**: Python 3.10
- **Libraries**: Requests, Pandas, Pathlib, Logging
- **Frontend**: Vanilla JS, CSS3 (Glassmorphism), HTML5
- **Tooling**: GitHub Actions (simulated), Vercel

## Core Accomplishments
1.  **Extraction Efficiency**: Built a paginated extractor that safely buffers up to 100+ records from a REST API.
2.  **Data Quality**: Implemented a transformation layer that handles null values, normalizes categories, and performs schema enforcement.
3.  **Business Intelligence**: Added a feature engineering step that calculates real-time inventory values ($), crucial for warehouse reporting.
4.  **Full-Stack Visibility**: Created a high-performance web dashboard that directly consumes the ETL output, showcasing the end-to-end data value chain.

## Challenges Resolved
- **Pagination Overhead**: Managed offset-based pagination to prevent memory overflow during high-volume extractions.
- **Type Safety**: Enforced strict numerical casting to ensure financial calculations (price/discount) are consistent across datasets.

---
*Ready for deployment to production environments.*
