import React from "react";
import { Button, Form, FormGroup, Input, Label } from "reactstrap";

import axios from "axios";

import { API_URL } from "../constants";

class NewStudentForm extends React.Component {
    state = {
        pk: 0,
        name: "",
        email: "",
        document: "",
        password: ""
    };

    componentDidMount() {
        if (this.props.student) {
            const { pk, name, document, email, password } = this.props.student;
            this.setState({ pk, name, document, email, password });
        }
    }

    onChange = e => {
        this.setState({ [e.target.name]: e.target.value });
    };

    createStudent = e => {
        e.preventDefault();
        axios.post(API_URL, this.state).then(() => {
            this.props.resetState();
            this.props.toggle();
        });
    };

    editStudent = e => {
        e.preventDefault();
        axios.put(API_URL + this.state.pk, this.state).then(() => {
            this.props.resetState();
            this.props.toggle();
        });
    };

    defaultIfEmpty = value => {
        return value === "" ? "" : value;
    };

    render() {
        return (
            <Form onSubmit={this.props.student ? this.editStudent : this.createStudent}>
                <FormGroup>
                    <Label for="name">Name:</Label>
                    <Input
                        type="text"
                        name="name"
                        onChange={this.onChange}
                        value={this.defaultIfEmpty(this.state.name)}
                    />
                </FormGroup>
                <FormGroup>
                    <Label for="email">Email:</Label>
                    <Input
                        type="email"
                        name="email"
                        onChange={this.onChange}
                        value={this.defaultIfEmpty(this.state.email)}
                    />
                </FormGroup>
                <FormGroup>
                    <Label for="document">Document:</Label>
                    <Input
                        type="text"
                        name="document"
                        onChange={this.onChange}
                        value={this.defaultIfEmpty(this.state.document)}
                    />
                </FormGroup>
                <FormGroup>
                    <Label for="password">Password:</Label>
                    <Input
                        type="text"
                        name="password"
                        onChange={this.onChange}
                        value={this.defaultIfEmpty(this.state.password)}
                    />
                </FormGroup>
                <Button>Send</Button>
            </Form>
        );
    }
}

export default NewStudentForm;