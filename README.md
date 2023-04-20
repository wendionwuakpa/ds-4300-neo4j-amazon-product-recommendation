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
Picture this: you're sitting at your computer, scrolling through Amazon's vast array of products, feeling more overwhelmed by the minute. You've been searching for the perfect item for what feels like hours, and you're about ready to give up.

But just as you're about to throw in the towel, you stumble upon a program that promises to be your own personal product recommender aka shopping assistant. Finally, some help!

As you start to navigate through the program, you can't help but marvel at the sheer size of Amazon's consumer base. After all, it's the largest shopping platform on the internet, with over 40% of all online purchases being made through Amazon.com.

But then you learn the shocking truth - Amazon's recommendation algorithm isn't designed around the consumer. In fact, it favors profit over the optimal choice for the shopper. It's no wonder you've been struggling to find the perfect product!

Thankfully, this program is different. It puts you - the consumer - first, by recommending products tailored to your needs and preferences. No more endless scrolling through irrelevant items. With this program, you can select a category and filter the products based on your budget.

But that's not all. The program takes it a step further by presenting you with five random products that fit your criteria. You get to choose your two favorites, and those choices are then used to generate personalized recommendations just for you.

It's like having your own personal shopping concierge, but without the expensive price tag. No more buyer's remorse or settling for subpar products. With this program, you'll finally have a shopping experience that puts your needs first.

## License

This project is licensed under the NEU.

## Contact

For questions or support, please contact any of the contributors

## Acknowledgments

Special thanks to Professor John Rachlin for guidance and support throughout the project.
