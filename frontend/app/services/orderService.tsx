import api from "./api";

// Tipo para pedidos existentes (com ID)
interface Order {
    id: number;
    table_id: number;
    total_price: number;
}


// Tipo para novos pedidos (sem ID)
export interface NewOrder {
    table_id: number;
    items: OrderItem[]; // inclui os itens
}



export interface OrderItem {
    menu_item_id: number;
    quantity: number;
}


export const getOrders = async (): Promise<Order[]> => {
    const response = await api.get("/orders");
    return response.data;
};

// Criar pedido com o tipo correto
export const createOrder = async (orderData: NewOrder): Promise<Order> => {
    const response = await api.post("/orders", orderData);
    return response.data;
};

export const closeOrder = async (orderId: number): Promise<Order> => {
    const response = await api.delete(`/orders/${orderId}`);
    return response.data;
};


// Fechar uma mesa pelo ID
export const closeTable = async (tableId: number): Promise<{ message: string }> => {
    const response = await api.post(`/tables/${tableId}/close`);
    return response.data;
};


export const getMenuItems = async () => {
    const response = await api.get("/menu-items");
    return response.data;
};


