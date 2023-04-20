# DS4300 Final Project: Consumer-Focused Amazon Product Recommendation Engine 

This project is an Amazon recommendation engine that uses Neo4j and Python to recommend products based on users' previously liked products. 

Our implementation introduces a more objective approach to Amazon's recommendation algorithm that prioritizes consumer preferences over profit-driven motivations. The project aims to create an engine that provides reasonable recommendations for products within a similar budget range and category, with a focus on objective criteria such as product category, price, and ratings. The approach is different from Amazon's algorithm, which tends to promote products from its in-house brands. The project uses the Neo4j Graph Database to create relationships between products and provide recommendations based on the most closely related products.

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

## Potential User Use-case Story
Imagine you are on Amazon, looking for a perfect product but you just can't seem to find the right one. It can be overwhelming, right? That's where this program comes in! It's like having your own personal shopping assistant that recommends products tailored to your needs and preferences.

To get started, the program prompts you to select a category for the type of product you're interested in. No need to spend hours scrolling through pages of irrelevant products anymore! The program then filters the products within that category based on the maximum price you're willing to pay.

But wait, it gets even better! The program then presents you with five random products that fit your selected category and price range. And the best part? You get to choose your two favorite products out of the five presented. Your favorites are then stored in a list and used to generate personalized product recommendations just for you.

No more endless searching for the perfect product. With this program, you'll have access to a selection of products that meet your specific needs and preferences. Say goodbye to buyer's remorse and hello to a personalized shopping experience!

## License

This project is licensed under the NEU.

## Contact

For questions or support, please contact any of the contributors

## Acknowledgments

Special thanks to Professor John Rachlin for guidance and support throughout the project.
