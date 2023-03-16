import { useState } from "react";
import { useForm } from "react-hook-form";
import { yupResolver } from '@hookform/resolvers/yup';
import API_REGISTER_URL from '../constants.js'
import * as yup from "yup";

const NUMBR_REGEX = /\d/;
const UPPERCASE_REGEX = /[A-Z]/;
const LOWERCASE_REGEX = /[a-z]/;
const SPECIAL_CHARACTER_REGEX = /[#?!@$%^&*-]/;

const schema = yup.object({
    username: yup.string().required().test({
        name: 'valid-username',
        test(value, ctx) {
          if (!isNaN(value[0])) {
            return ctx.createError({ message: 'Username cannot start with a number'})
          }
          if (value.length < 5) {
            return ctx.createError({ message: 'Username must have at least 5 characters' })
          }
          return true
        }
    }),
    email: yup.string().email().required(),
    password: yup.string().required().test({
        name: 'valid-password',
        test(value, ctx) {
          if (!NUMBR_REGEX.test(value)) {
            return ctx.createError({ message: 'Password must contains at least 1 number'})
          }
          if (!UPPERCASE_REGEX.test(value)) {
            return ctx.createError({ message: 'Password must contains at least 1 upper case letter'})
          }
          if (!LOWERCASE_REGEX.test(value)) {
            return ctx.createError({ message: 'Password must contains at least 1 lower case letter'})
          }
          if (!SPECIAL_CHARACTER_REGEX.test(value)) {
            return ctx.createError({ message: 'Password must contains at least 1 special charater'})
          }
          if (value.length < 8) {
            return ctx.createError({ message: 'Password must have at least 8 characters' })
          }
          return true
        }
    }),
    passwordConfirmation: yup.string()
     .oneOf([yup.ref('password'), null], 'Passwords must match')
  }).required();

const Register = () => {
    const [isPending,setIsPending] = useState(false);
    const [fetchError,setFetchError] = useState(null);

    const { register, handleSubmit, formState: { errors } } = useForm(
        {resolver: yupResolver(schema)}
    );
    
    const onSubmit = (data, e) => {
        e.preventDefault();

        setIsPending(true);
        const {username, email, password} = data

        fetch(API_REGISTER_URL, {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({username, email, password})
        }).then(res => {
            if(!res.ok){
                throw Error('Could not create a user');
            }
            setIsPending(false);
            setFetchError(null);
            
        }).catch(err => {
            setIsPending(false);
            setFetchError(err.message);
        })
    }

    return ( 
        <div className="section container">
            <div className="row">
                <h3 className="center">User registration form</h3>
            </div>
            <div className="row">
                <form onSubmit={handleSubmit(onSubmit)}>
                    <label>
                        Username:
                        <input 
                            type="text"
                            {...register("username")} 
                        />
                        <p className="red-text">{errors.username?.message}</p>
                    </label>
                    <label>
                        Email:
                        <input
                            type="text"
                            {...register("email")}
                        />
                        <p className="red-text">{errors.email?.message}</p>
                    </label>
                    <label>
                        Password:
                        <input 
                            type="password"
                            {...register("password")}
                        />
                        <p className="red-text">{errors.password?.message}</p>
                    </label>
                    <label>
                        Confirm password:
                        <input 
                            type="password"
                            {...register("passwordConfirmation")}
                        />
                        <p className="red-text">{errors.passwordConfirmation?.message}</p>
                    </label>
                    {!isPending && <button className="btn">Create user</button>}
                    {isPending && <button className="btn" disabled>Creating user...</button>}
                </form>
            </div>
            {fetchError && <div className="row red-text">{fetchError}</div>}
        </div>
     );
}
 
export default Register;