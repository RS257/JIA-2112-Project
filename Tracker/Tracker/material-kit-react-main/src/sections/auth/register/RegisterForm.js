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
import Iconify from '../../../components/Iconify';
import { FormProvider, RHFTextField } from '../../../components/hook-form';
import {API_URL} from "../../../constants";

// ----------------------------------------------------------------------

export default function RegisterForm(props) {
  const navigate = useNavigate();

  const [showPassword, setShowPassword] = useState(false);

  // const RegisterSchema = Yup.object().shape({
  //   firstName: Yup.string().required('First name required'),
  //   lastName: Yup.string().required('Last name required'),
  //   email: Yup.string().email('Email must be a valid email address').required('Email is required'),
  //   password: Yup.string().required('Password is required'),
  // });

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
              onClick={createStudent}
          >
            Register
          </Button>
        </Stack>
      </div>
  );
}
