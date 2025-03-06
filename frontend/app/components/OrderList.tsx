"use client";

import React, { useEffect, useState } from "react";
import { getOrders, closeTable } from "../services/orderService";
import { Title, Subtitle, Text } from "./styles";
import { Button } from "./ui/button";
import styled from "styled-components";

interface Order {
    id: number;
    table_id: number;
    total_price: number;
}

interface TableOrders {
    table_id: number;
    orders: Order[];
    total: number;
    status: string;
}

const TOTAL_TABLES = 5;

const Card = styled.div`
    background: white;
    padding: 16px;
    border-radius: 12px;
    box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
    border: 1px solid #ddd;
`;

const Badge = styled.span<{ status: string }>`
    padding: 6px 12px;
    border-radius: 20px;
    font-weight: bold;
    color: white;
    background: ${({ status }) => (status === "aberta" ? "#28a745" : "#dc3545")};
`;

const OrderList: React.FC = () => {
    const [tables, setTables] = useState<TableOrders[]>([]);

    useEffect(() => {
        const fetchOrders = async () => {
            const orders = await getOrders();
            
            const tableData: Record<number, TableOrders> = {};
            for (let i = 1; i <= TOTAL_TABLES; i++) {
                tableData[i] = { table_id: i, orders: [], total: 0, status: "fechada" };
            }

            orders.forEach(order => {
                if (!tableData[order.table_id]) {
                    tableData[order.table_id] = { table_id: order.table_id, orders: [], total: 0, status: "fechada" };
                }
                tableData[order.table_id].orders.push(order);
                tableData[order.table_id].total += order.total_price;
                tableData[order.table_id].status = "aberta";
            });

            setTables(Object.values(tableData));
        };
        
        fetchOrders();
    }, []);

    const handleCloseTable = async (tableId: number) => {
        await closeTable(tableId);
        setTables(prevTables => prevTables.map(table => 
            table.table_id === tableId ? { ...table, orders: [], total: 0, status: "fechada" } : table
        ));
    };

    return (
        <div className="p-4 max-w-2xl mx-auto">
            <Title>Lista de Mesas e Pedidos</Title>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                {tables.map((table) => (
                    <Card key={table.table_id}>
                        <div className="flex justify-between items-center mb-2">
                            <Subtitle>Mesa {table.table_id}</Subtitle>
                            <Badge status={table.status}>{table.status.toUpperCase()}</Badge>
                        </div>
                        <Text className="font-semibold">Total: <span className="text-lg text-green-700 font-bold">R$ {(table.total / 100).toFixed(2)}</span></Text>
                        <ul className="mt-3 space-y-2">
                            {table.orders.map((order) => (
                                <li key={order.id} className="p-2 bg-gray-50 border rounded-lg flex justify-between items-center">
                                    <Text>Pedido {order.id}</Text>
                                    <span className="text-green-700 font-bold">R$ {(order.total_price / 100).toFixed(2)}</span>
                                </li>
                            ))}
                        </ul>
                        {table.status === "aberta" && (
                            <Button className="mt-3 w-full bg-red-600 hover:bg-red-700 text-white py-2 rounded-lg" onClick={() => handleCloseTable(table.table_id)}>
                                Fechar Conta
                            </Button>
                        )}
                    </Card>
                ))}
            </div>
        </div>
    );
};

export default OrderList;
