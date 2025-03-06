"use client";

import React from "react";
import styled from "styled-components";

interface ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
    variant?: "primary" | "secondary" | "danger";
}

const StyledButton = styled.button<ButtonProps>`
    padding: 10px 16px;
    border-radius: 6px;
    font-size: 16px;
    font-weight: 500;
    cursor: pointer;
    transition: background 0.2s ease-in-out;
    border: none;

    ${(props) =>
        props.variant === "primary" &&
        `
        background: #2563eb;
        color: white;
        &:hover {
            background: #1d4ed8;
        }
    `}

    ${(props) =>
        props.variant === "secondary" &&
        `
        background: #e5e7eb;
        color: black;
        &:hover {
            background: #d1d5db;
        }
    `}

    ${(props) =>
        props.variant === "danger" &&
        `
        background: #dc2626;
        color: white;
        &:hover {
            background: #b91c1c;
        }
    `}
`;

const Button: React.FC<ButtonProps> = ({ variant = "primary", children, ...props }) => {
    return (
        <StyledButton variant={variant} {...props}>
            {children}
        </StyledButton>
    );
};

export { Button };
