import React from "react";
import type { Product, CartAction } from "./types";

type ProductListProps = {
  products: Product[];
  dispatch: React.Dispatch<CartAction>;
};

export const ProductList = ({ products, dispatch }: ProductListProps) => {
  const handleAddToCart = (product: Product) => {
    dispatch({ type: "ADD_ITEM", payload: product });
  };
  return (
    <div>
      <h3>Products</h3>
      {products.map((p) => (
        <div key={p.id}>
          {p.name} - ${p.price}
          <button
            onClick={() => handleAddToCart(p)}
            style={{ marginLeft: "10px" }}
          >
            Add to Cart
          </button>
        </div>
      ))}
    </div>
  );
};
