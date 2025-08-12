import React from "react";

import type { CartState, CartAction } from "./types";

type CartDisplayProps = {
  cartState: CartState;
  dispatch: React.Dispatch<CartAction>;
};

export const CartDisplay = ({ cartState, dispatch }: CartDisplayProps) => {
  const total = cartState.items.reduce(
    (sum, item) => sum + item.price * item.quantity,
    0
  );

  return (
    <div
      style={{ marginTop: "20px", border: "1px solid #ccc", padding: "10px" }}
    >
      {cartState.items.length === 0 ? (
        <p>Your cart is empty.</p>
      ) : (
        <>
          {cartState.items.map((item) => (
            <div key={item.id}>
              {item.name} (x {item.quantity}) - ${item.price * item.quantity}
              <button
                onClick={() =>
                  dispatch({
                    type: "REMOVE_ITEM",
                    payload: { id: item.id },
                  })
                }
                style={{ marginLeft: "10px" }}
              >
                Remove
              </button>
            </div>
          ))}
          <hr />
          <p>
            <strong>Total: ${total.toFixed(2)}</strong>
          </p>
          <button
            onClick={() =>
              dispatch({
                type: "CLEAR_CART",
              })
            }
          >
            Clear Cart
          </button>
        </>
      )}
    </div>
  );
};
