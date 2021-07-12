import React from "react";
import styled from "styled-components";

export const ButtonPrimary = styled.button`
    cursor: pointer;
    display: inline-block;
    border: none;
    padding: 1rem 2rem;
	   border-radius: 4px;
    margin: 8px;
    text-decoration: none;
    background: #0069ed;
    color: #ffffff;
    font-family: sans-serif;
    font-size: 1.2rem;
    cursor: pointer;
    text-align: center;
    transition: background 250ms ease-in-out, 
                transform 150ms ease;
    -webkit-appearance: none;
    -moz-appearance: none;
`

export const VoteYesButton = styled()

function VoteButton({ triggerEvent, text }) {
    return (
        <div>
        <button className="vote-yes">{upArrow}</button>
            <button className = "vote-no">{downArrow}</button>
        </div>
    )
}

export default VoteButton;