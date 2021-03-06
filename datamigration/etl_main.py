import logging
import os

from etl_product import Product
from etl_ingredient import Ingredient
from etl_descrip import Descrip
from etl_relation import Relation

def init_logger():

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    # log 출력 형식
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    # log 출력
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    # log를 파일에 출력
    file_handler = logging.FileHandler("error.log")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger

logger = init_logger()

'''
Data Load 순서
Ingredient ,Product > descrip > ProductIngredientRelation 
'''

def main() :
  
  #product
  print("migration start - product")
  ex = Product().load_data()
  if ex is not None :
    logger.info(f'product - {ex}')
    exit()
  else :
    logger.info("migration product")
  
  #igredient 
  print("migration start - ingredient")
  ex = Ingredient().load_data()
  if ex is not None :
    logger.info(f'ingredient - {ex}')
    exit()
  else :
    logger.info("migration ingredient")

  #descrip 
  print("migration start - descrip")
  ex = Descrip().load_data()
  if ex is not None :
    logger.info(f'descrip - {ex}')
    exit()
  else :
    logger.info("migration descrip")

  #relation 
  print("migration start - product_ingredient_relation")
  ex = Relation().load_data()
  if ex is not None :
    logger.info(f'product_ingredient_relation - {ex}')
    exit()
  else :
    logger.info("migration product_ingredient_relation")

if __name__ == "__main__":
    main()
