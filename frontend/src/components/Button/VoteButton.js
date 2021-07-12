import React from "react";
import styled from "styled-components";
import { FontAwesomeIcon } from "'@fortawesome/react-fontawesome'"
import { faThumbsUp, faThumbsDown } from "@fortawesome/free-solid-svg-icons"

const upArrow = <FontAwesomeIcon icon={faThumbsUp} />
const downArrow = <FontAwesomeIcon icon={faThumbsDown} />

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

export const VoteYesButton = styled(ButtonPrimary)`
    background: #80c904;
`

export const VoteNoButton = styled(ButtonPrimary)`
    background: #FF6666;
    :hover {
        background: white;
    }
`

function VoteButton({ triggerEvent, text }) {
    return (
        <div>
            <VoteYesButton>{upArrow}</VoteYesButton>
            <VoteNoButton>{downArrow}</VoteNoButton>
        </div>
    )
}

export default VoteButton;