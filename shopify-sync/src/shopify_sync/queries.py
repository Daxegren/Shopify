"""GraphQL-frågor för Shopify Bulk Operations.

`{filter}` ersätts med en sökfilter-sträng, t.ex. `updated_at:>='2026-01-01T00:00:00Z'`.
Nästlade connections (lineItems, variants) kommer som egna JSONL-rader med `__parentId`.
"""

ORDERS = """
{
  orders(query: "{filter}", sortKey: UPDATED_AT) {
    edges {
      node {
        id
        name
        createdAt
        updatedAt
        processedAt
        cancelledAt
        closedAt
        displayFinancialStatus
        displayFulfillmentStatus
        currencyCode
        totalPriceSet { shopMoney { amount currencyCode } }
        currentTotalPriceSet { shopMoney { amount } }
        subtotalPriceSet { shopMoney { amount } }
        totalDiscountsSet { shopMoney { amount } }
        totalShippingPriceSet { shopMoney { amount } }
        totalTaxSet { shopMoney { amount } }
        totalRefundedSet { shopMoney { amount } }
        discountCodes
        sourceName
        customer { id }
        shippingAddress { countryCodeV2 }
        customerJourneySummary {
          firstVisit {
            source
            landingPage
            utmParameters { source medium campaign }
          }
          lastVisit {
            source
            utmParameters { source medium campaign }
          }
        }
        refunds {
          id
          createdAt
          totalRefundedSet { shopMoney { amount } }
        }
        lineItems {
          edges {
            node {
              id
              sku
              title
              variantTitle
              vendor
              quantity
              currentQuantity
              product { id }
              variant { id }
              originalUnitPriceSet { shopMoney { amount } }
              discountedTotalSet { shopMoney { amount } }
            }
          }
        }
      }
    }
  }
}
"""

PRODUCTS = """
{
  products(query: "{filter}", sortKey: UPDATED_AT) {
    edges {
      node {
        id
        handle
        title
        status
        vendor
        productType
        tags
        createdAt
        updatedAt
        publishedAt
        totalInventory
        onlineStoreUrl
        seo { title description }
        variants {
          edges {
            node {
              id
              sku
              title
              barcode
              price
              compareAtPrice
              inventoryQuantity
              createdAt
              updatedAt
              inventoryItem { id unitCost { amount } }
            }
          }
        }
      }
    }
  }
}
"""

# Inga direkta personuppgifter hämtas.
CUSTOMERS = """
{
  customers(query: "{filter}", sortKey: UPDATED_AT) {
    edges {
      node {
        id
        createdAt
        updatedAt
        numberOfOrders
        amountSpent { amount currencyCode }
        tags
        defaultAddress { countryCodeV2 }
      }
    }
  }
}
"""

BY_ENTITY = {
    "orders": ORDERS,
    "products": PRODUCTS,
    "customers": CUSTOMERS,
}


def build(entity: str, filter_: str) -> str:
    # str.format krockar med GraphQL:s klammerparenteser, därför replace.
    return BY_ENTITY[entity].replace("{filter}", filter_.replace('"', '\\"'))
