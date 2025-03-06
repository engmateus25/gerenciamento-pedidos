import styled from "styled-components";

export const Title = styled.h1`
    font-size: 2rem;  /* Maior que o padrão */
    font-weight: bold;
    text-align: center;
    margin-bottom: 1.5rem;
    color: #1a202c;  /* Um tom de cinza escuro */
`;

export const Subtitle = styled.h2`
    font-size: 1.5rem;
    font-weight: 600;
    text-align: center;
    margin-bottom: 1rem;
    color: #2d3748; /* Um pouco mais claro que o Title */
`;

export const Text = styled.p`
    font-size: 1rem;
    line-height: 1.5;
    color: #4a5568; /* Tom de cinza escuro para textos comuns */
`;
