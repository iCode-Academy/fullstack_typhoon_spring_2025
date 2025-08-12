import React, {useReducer} from "react";

import { ProductList } from "./ProductList";
import { CartDisplay } from "./CartDisplay";
import type { CartState, CartAction, Product } from "./types";


const cartReducer = (state: CartState, action: CartAction): 
        CartState => {
            switch(action.type) {
                case 'ADD_ITEM': {
                    const existingItem = state.items.find((item) => item.id === action.payload.id)
                    if (existingItem) {
                        return {
                            ...state,
                            items: state.items.map((item) => item.id === action.payload.id ? {
                                ...item, quantity: item.quantity + 1
                            }: item)
                        }
                    }
                    return {
                        ...state,
                        items: [...state.items, {
                            ...action.payload, quantity: 1
                        }]
                    }
                }
                case 'REMOVE_ITEM':
                    return {
                        ...state,
                        items: state.items.filter((item) => item.id !== action.payload.id),
                    }
                case 'CLEAR_CART':
                    return {
                        items: []
                    }
                default:
                    return state;
            }
}

const availableProducts: Product[] = [
    {id: 1, name: 'React T-Shirt', price: 25},
    {id: 2, name: 'Typescript Mag', price: 15},
    {id: 3, name: 'useState Sticker', price: 5},
]

const CartPage = () => {
    const [state, dispatch] = useReducer(cartReducer, {items: []});

    return(
        <div>
            <h2>Reducer Shopping Cart</h2>
            <ProductList products={availableProducts} dispatch={dispatch}/>
            <CartDisplay cartState={state} dispatch={dispatch} />
        </div>
    )
}
export default CartPage;