import React, { useEffect, useState } from "react";
import { Container } from "react-bootstrap";
import { Card, Col, Row } from "react-bootstrap";
import { useLocation, useHistory } from "react-router-dom";
import movieApi from "../services/movie";
import "../style/pages/SearchResult.scss";

function ResultItem(movie) {
    const history = useHistory();

    const handleOnClick = () => {
        history.push(`/movies/${movie.id}`);
    };

    return (
        <Card className="resultItem" onClick={(e) => handleOnClick(e)}>
            <Card.Body className="resultItem__body">
                <Row>
                    <Col md="2" className="resultItem--left">
                        <img src={movie.poster} alt="" className="resultItem__poster" />
                    </Col>
                    <Col md="10" className="resultItem--right">
                        <div className="resultItem__author">
                            <h3>{movie.title}</h3>
                            <small>{movie.year}</small>
                        </div>

                        <Card.Text className="resultItem__list">{movie.description}</Card.Text>
                    </Col>
                </Row>
            </Card.Body>
        </Card>
    );
}

function useQuery() {
    return new URLSearchParams(useLocation().search);
}

function SearchResult() {
    const [movies, setMovies] = useState([]);
    const query = useQuery();

    useEffect(async () => {
        if (query.get("q")) {
            const searchText = query.get("q").replaceAll(" ", "+");
            const response = await movieApi.searchMovie(searchText);
            setMovies(response.results);
        }
    });

    return (
        <Container>
            <h3 className="title">Result search: {query.get("q")}</h3>
            {movies.length > 0 ? (
                movies?.map((movie) => {
                    return ResultItem(movie);
                })
            ) : (
                <p>Not found any movie</p>
            )}
        </Container>
    );
}

export default SearchResult;
