from typing import List

from fastapi import HTTPException, Request, Response, status
from sqlalchemy.orm import Session

import models as models

from .. import schemas


def get_product_by_category(db: Session, request: schemas.SearchCategory):
    largeCategory = request.largeCategory
    smallCategory = request.smallCategory

    searchLarge = "%{}%".format(largeCategory)
    searchSmall = "%{}%".format(smallCategory)

    currentPage = request.requestPage
    perPage = request.maxItemCountByPage

    offset = currentPage * perPage
    limit = offset + perPage

    productList = (
        db.query(models.Product)
        .join(models.Descrip)
        .filter(
            (models.Descrip.major_classification.like(searchLarge))
            & (models.Descrip.medium_classification.like(searchSmall))
        )
        .all()
    )
    showList = productList[offset:limit]

    listLen = len(productList)
    searchResult = schemas.SearchResult
    searchResult.totalPageCount = int(listLen / request.maxItemCountByPage)
    searchResult.currentPage = request.requestPage
    searchResult.result = showList
    return searchResult


def get_product_by_keyword(db: Session, request: schemas.SearchKeyword):
    search_keyword = request.keyword
    searchType = request.searchResultType
    search = "%{}%".format(search_keyword)

    currentPage = request.requestPage
    perPage = request.maxItemCountByPage

    offset = currentPage * perPage
    limit = offset + perPage
    if searchType == "product":
        productList = (
            db.query(models.Product).filter(models.Product.name.like(search)).all()
        )
        showList = productList[offset:limit]
    elif searchType == "brand":
        search = search.upper()
        productList = (
            db.query(models.Product).filter(models.Product.brand.like(search)).all()
        )
        showList = productList[offset:limit]
    # elif searchType == "ingredient":
    # firstFilter = (
    #     db.query(models.Ingredient.id)
    #     .filter(models.Ingredient.ko_ingredient.like(search))
    #     .all()
    # )
    # fistFilter=list(firstFilter)
    # secondFilter = (
    #     db.query(models.productingredientrelation.product_id)
    #     .filter(models.productingredientrelation.ingredient_id == id)
    #     .all()
    # )
    #
    listLen = len(productList)
    searchResult = schemas.SearchResult
    searchResult.totalPageCount = int(listLen / request.maxItemCountByPage)
    searchResult.currentPage = request.requestPage

    searchResult.result = showList
    return searchResult


# def get_product_by_ingredient(db:Session, request:schemas.SearchIngredients):
#     includeIngredient=request.includeIngredient
#     excludeIngredient=request.excludeIngredient
