import React from "react";
import { Card, Col, Row } from "react-bootstrap";
import "../style/components/CommentCard.scss";

function CommentCard() {
    return (
        <Card className="commendCard">
            <Card.Body>
                <Row>
                    <Col md="2" className="commendCard--left">
                        <img
                            src="https://www.themoviedb.org/t/p/w64_and_h64_face/xNLOqXXVJf9m7WngUMLIMFsjKgh.jpg"
                            alt=""
                            className="commendCard__avatar"
                        />
                    </Col>
                    <Col md="10" className="commendCard--right">
                        <div className="commendCard__author">
                            <h3>A review by JPV852</h3>
                            <small>March 31, 2021</small>
                        </div>

                        <Card.Text className="commendCard__list">
                            Satisfying through and through. Also they seemed to learn from the past mistakes (with
                            Godzilla and Godzilla: King of the Monsters) of doing too much with the human characters,
                            here they are thankfully just window dressing for the battle between the two titans.
                        </Card.Text>
                    </Col>
                </Row>
            </Card.Body>
        </Card>
    );
}

export default CommentCard;
