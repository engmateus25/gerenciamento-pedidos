"use client";

import React from "react";
import OrderList from "./components/OrderList";
import OrderForm from "./components/OrderForm";
import { Title } from "./components/styles";

const Home: React.FC = () => {
    return (
        <div className="min-h-screen bg-gray-50 p-10 flex flex-col items-center">
            <Title className="text-4xl font-bold text-gray-900 mb-10">Gerenciamento de Pedidos</Title>
            <div className="grid grid-cols-1 md:grid-cols-3 gap-12 w-full max-w-7xl">
                <div className="md:col-span-1 bg-white p-8 rounded-2xl shadow-xl border border-gray-300">
                    <OrderForm />
                </div>
                <div className="md:col-span-2 bg-white p-8 rounded-2xl shadow-xl border border-gray-300">
                    <OrderList />
                </div>
            </div>
        </div>
    );
};

export default Home;
