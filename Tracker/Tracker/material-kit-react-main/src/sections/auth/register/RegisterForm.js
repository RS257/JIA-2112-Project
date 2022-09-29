import axios from "axios";
import * as Yup from 'yup';

import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
// form
import { useForm } from 'react-hook-form';
import { yupResolver } from '@hookform/resolvers/yup';
// @mui
import {
  Stack,
  IconButton,
  InputAdornment,
  TextField,
  Button,
  FormControl,
  InputLabel,
  OutlinedInput
} from '@mui/material';
import Visibility from '@mui/icons-material/Visibility';
import VisibilityOff from '@mui/icons-material/VisibilityOff';
import { LoadingButton } from '@mui/lab';
// components
import {API_URL} from "../../../constants";
/* eslint-disable camelcase */

// ----------------------------------------------------------------------

export default function RegisterForm(props) {
  const navigate = useNavigate();

  const [showPassword, setShowPassword] = useState(false);

  const [state, setState] = useState({
    firstName: '',
    lastName: '',
    email: "",
    password: '',
  });

  const onSubmit = async () => {
    navigate('/dashboard', { replace: true });
  };

  const onChange = e => {
    // this.setState({ [e.target.name]: e.target.value });
    state[e.target.name] = e.target.value
    setState({ ...state })
  };

  const createStudent = e => {
    e.preventDefault();

    const newStudent = {
      firstName: state.firstName,
      lastName: state.lastName,
      email: state.email,
      password: state.password
    };
    axios.post(API_URL, newStudent).then(() => {
      props.resetState();
    });
    navigate('/login', { replace: true });
  };

  const addUser = async () => {
    const username = 'testuser'
    const email = state.email
    const password = state.password
    const password2 = state.password
    const first_name = state.firstName
    const last_name = state.lastName
    const response = await fetch("http://127.0.0.1:8000/accounts/register/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        username,
        password,
        password2,
        email,
        first_name,
        last_name,
      })
    })
    if (response.status === 201) {
      // alert("login");
    } else {
      alert("Something went wrong!");
    }
  };

  return (
      <div>
        <Stack spacing={3}>
          <Stack direction={{ xs: 'column', sm: 'row' }} spacing={2}>
            <TextField
                required
                id="outlined-required"
                name="firstName"
                label="First name"
                value={state.firstName}
                onChange={onChange}
            />
            <TextField
                required
                id="outlined-required"
                name="lastName"
                label="Last name"
                value={state.lastName}
                onChange={onChange}
            />
          </Stack>

          <TextField
              required
              id="outlined-required"
              name="email"
              label="Email address"
              value={state.email}
              onChange={onChange}
          />

          <FormControl sx={{ m: 1, width: '25ch' }} variant="outlined">
            <InputLabel htmlFor="outlined-adornment-password">Password</InputLabel>
            <OutlinedInput
                id="outlined-adornment-password"
                type={showPassword ? 'text' : 'password'}
                value={state.password}
                name="password"
                onChange={onChange}
                endAdornment={
                  <InputAdornment position="end">
                    <IconButton
                        aria-label="toggle password visibility"
                        onClick={() => setShowPassword(!showPassword)}
                        edge="end"
                    >
                      {showPassword ? <VisibilityOff /> : <Visibility />}
                    </IconButton>
                  </InputAdornment>
                }
                label="Password"
            />
          </FormControl>

          <Button
              variant="contained"
              onClick={addUser}
          >
            Add User
          </Button>

          <Button
              variant="contained"
              onClick={addUser}
          >
            Register
          </Button>
        </Stack>
      </div>
  );
}
