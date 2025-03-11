import api from "./api";


interface Order {
    id: number;
    table_id: number;
    total_price: number;
}


export interface NewOrder {
    table_id: number;
    items: OrderItem[]; 
}


export interface OrderItem {
    menu_item_id: number;
    quantity: number;
}


export const getOrders = async (): Promise<Order[]> => {
    const response = await api.get("/orders");
    return response.data;
};


export const createOrder = async (orderData: NewOrder): Promise<Order> => {
    const response = await api.post("/orders", orderData);
    return response.data;
};

export const closeOrder = async (orderId: number): Promise<Order> => {
    const response = await api.delete(`/orders/${orderId}`);
    return response.data;
};


export const closeTable = async (tableId: number): Promise<{ message: string }> => {
    const response = await api.post(`/tables/${tableId}/close`);
    return response.data;
};


export const getMenuItems = async () => {
    const response = await api.get("/menu-items");
    return response.data;
};


