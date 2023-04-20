# DS4300 Final Project: Consumer-Focused Amazon Product Recommendation Engine 

This project is an Amazon recommendation engine that uses Neo4j and Python to recommend products based on users' previously liked products. 

Our implementation introduces a novel approach to Amazon's recommendation algorithm that prioritizes consumer preferences over profit-driven motivations. The project aims to create an engine that provides reasonable recommendations for products within a similar budget range and category, with a focus on objective criteria such as product category, price, and ratings. The approach is different from Amazon's algorithm, which tends to promote products from its in-house brands. The project uses the Neo4j Graph Database to create relationships between products and provide recommendations based on the most closely related products.

To run the project, follow these steps:

## Requirements

- Neo4j
- Python 3.6+

## Installation

1. Clone the project repository to your local machine.
2. Install the required Python packages using the following command:

   ```
   pip install -r requirements.txt
   ```

## Usage

1. Make sure that the `amazon.csv` file is in the same directory as the `DS4300_Project.ipynb` file.
2. Start Neo4j on your local machine and create a new graph database.
3. Open the `DS4300_Project.ipynb' file and update the `uri`, `username`, and `password` variables with your Neo4j database credentials.
4. Run the following command to start the recommendation engine:

   ```
   run python DS4300_Project.ipynb
   ```

   This will load the data from `amazon.csv` into your Neo4j database and start the recommendation engine.
   
5. Follow the prompts in the command line interface to input user information and get product recommendations.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more information.

## Contact

For questions or support, please contact the project maintainer at [maintainer@example.com](mailto:maintainer@example.com).

## Acknowledgments

Special thanks to Professor Jane Smith for guidance and support throughout the project.
