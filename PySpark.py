from pyspark.sql.functions import col


def get_product_categories(product_df, categories_df):
    # объединяем таблицы продуктов и категорий по полю product_id
    joined_df = product_df.join(categories_df, "product_id")
    # применяемleftOuterJoin # к таблице продуктов и полученной таблице
    result_df = product_df.join(joined_df, "product_id", "left_outer").select("product_name", 'category_name')
    return result_df

