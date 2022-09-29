/* eslint-disable camelcase */

import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import jwt_decode from "jwt-decode";
// form
// @mui
import {
    Link,
    Stack,
    IconButton,
    InputAdornment,
    Button,
    TextField,
    InputLabel,
    OutlinedInput,
    FormControl, Checkbox, FormControlLabel
} from '@mui/material';
import { LoadingButton } from '@mui/lab';
// components
import VisibilityOff from "@mui/icons-material/VisibilityOff";
import Visibility from "@mui/icons-material/Visibility";
import account from "../../../_mock/account";

// ----------------------------------------------------------------------

export default function LoginForm() {
  const navigate = useNavigate();

  const [showPassword, setShowPassword] = useState(false);

    const [state, setState] = useState({
        email: "",
        password: '',
    });

    const [authTokens, setAuthTokens] = useState(() =>
        localStorage.getItem("authTokens")
            ? JSON.parse(localStorage.getItem("authTokens"))
            : null
    );
    const [user, setUser] = useState(() =>
        localStorage.getItem("authTokens")
            ? jwt_decode(localStorage.getItem("authTokens"))
            : null
    );

    const onChange = e => {
        state[e.target.name] = e.target.value
        setState({ ...state })
    };

  const defaultValues = {
    email: '',
    password: '',
    remember: true,
  };

  const onSubmit = async () => {
      navigate('/dashboard', { replace: true });
  };

    const loginUser = async () => {
        const username = 'testuserx'
        const password = 'testpassx'
        const response = await fetch("http://127.0.0.1:8000/accounts/token/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                username,
                password
            })
        });
        const data = await response.json();

        if (response.status === 200) {
            setAuthTokens(data);
            setUser(jwt_decode(data.access));
            localStorage.setItem("authTokens", JSON.stringify(data));
            alert(jwt_decode(data.access).email)
        } else {
            alert("Login failure");
        }
    };

  return (
    <div>
        <Stack spacing={3}>
            <TextField
                required
                id="outlined-required"
                name="email"
                label="Email address"
                value={state.email}
                onChange={onChange}
            />

            <FormControl sx={{ m: 1 }} variant="outlined">
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

            <Stack direction="row" alignItems="center" justifyContent="space-between" sx={{ my: 2 }}>
                <FormControlLabel control={<Checkbox defaultChecked />} label="Remember me" />
                <Link variant="subtitle2" underline="hover">
                    Forgot password?
                </Link>
            </Stack>

            <Button
                variant="contained"
                onClick={loginUser}
                fullwidth
            >
                Login
            </Button>
        </Stack>
    </div>
  );
}
