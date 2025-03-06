"use client";

import React, { useState, useEffect } from "react";
import { createOrder, getMenuItems } from "../services/orderService";
import { Title, Subtitle, Text } from "./styles";
import { Button } from "./ui/button";
import styled from "styled-components";

interface MenuItem {
    id: number;
    name: string;
    price: number;
}

interface OrderItem {
    menu_item_id: number;
    quantity: number;
}

const Input = styled.input`
    width: 100%;
    padding: 12px;
    border: 2px solid #ccc;
    border-radius: 8px;
    font-size: 1rem;
    color: #333;
    outline: none;
    &:focus {
        border-color: #007bff;
    }
`;

const OrderForm: React.FC = () => {
    const [tableId, setTableId] = useState<number | "">("");
    const [menuItems, setMenuItems] = useState<MenuItem[]>([]);
    const [selectedItems, setSelectedItems] = useState<OrderItem[]>([]);

    useEffect(() => {
        const fetchMenuItems = async () => {
            try {
                const data = await getMenuItems();
                setMenuItems(data);
            } catch (error) {
                console.error("Erro ao buscar itens do menu:", error);
            }
        };
        fetchMenuItems();
    }, []);

    const handleAddItem = (menuItemId: number) => {
        setSelectedItems((prevItems) => {
            const existingItem = prevItems.find((item) => item.menu_item_id === menuItemId);

            if (existingItem) {
                return prevItems.map((item) =>
                    item.menu_item_id === menuItemId
                        ? { ...item, quantity: item.quantity + 1 }
                        : item
                );
            } else {
                return [...prevItems, { menu_item_id: menuItemId, quantity: 1 }];
            }
        });
    };

    const calculateTotal = () => {
        return selectedItems.reduce((total, item) => {
            const menuItem = menuItems.find((menu) => menu.id === item.menu_item_id);
            return total + (menuItem ? menuItem.price * item.quantity : 0);
        }, 0);
    };

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        if (tableId === "" || selectedItems.length === 0) return;

        await createOrder({
            table_id: Number(tableId),
            items: selectedItems,
        });

        setTableId("");
        setSelectedItems([]);
        alert("Pedido criado com sucesso!");
    };

    return (
        <div className="p-6 max-w-lg mx-auto bg-white shadow-lg rounded-xl border border-gray-300">
            <Title>Novo Pedido</Title>
            <form onSubmit={handleSubmit} className="space-y-4">
                <div>
                    <Subtitle>Mesa</Subtitle>
                    <Input
                        type="number"
                        value={tableId}
                        onChange={(e) => {
                            const value = Number(e.target.value);
                            if (value >= 1 && value <= 5) {
                                setTableId(value);
                            }
                        }}
                        required
                    />
                </div>

                <div>
                    <Subtitle>Selecione os itens do menu</Subtitle>
                    <ul className="mt-2 space-y-2">
                        {menuItems.map((item) => (
                            <li key={item.id} className="flex justify-between items-center p-2 bg-gray-50 rounded-lg">
                                <Text>{item.name} - R$ {(item.price / 100).toFixed(2)}</Text>
                                <Button type="button" className="px-4 py-2 text-white bg-blue-600 hover:bg-blue-700 rounded-lg" onClick={() => handleAddItem(item.id)}>
                                    Adicionar
                                </Button>
                            </li>
                        ))}
                    </ul>
                </div>

                <div>
                    <Subtitle>Resumo do Pedido</Subtitle>
                    <ul className="mt-2 space-y-2">
                        {selectedItems.map((item) => {
                            const menuItem = menuItems.find((menu) => menu.id === item.menu_item_id);
                            return menuItem ? (
                                <li key={item.menu_item_id} className="p-2 bg-gray-50 rounded-lg">
                                    <Text>
                                        {menuItem.name} - {item.quantity}x = R$ {(menuItem.price * item.quantity / 100).toFixed(2)}
                                    </Text>
                                </li>
                            ) : null;
                        })}
                    </ul>
                    <Text className="font-bold text-lg">Total: R$ {(calculateTotal() / 100).toFixed(2)}</Text>
                </div>

                <Button type="submit" className="w-full py-3 text-lg text-white bg-green-600 hover:bg-green-700 rounded-lg">
                    Criar Pedido
                </Button>
            </form>
        </div>
    );
};

export default OrderForm;
