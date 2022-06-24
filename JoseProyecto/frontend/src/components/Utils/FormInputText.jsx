import * as React from 'react';
import { TextField} from '@mui/material';
import { FormControl, FormHelperText} from '@mui/material';
import { Controller} from "react-hook-form";

export default function FormInputText({ name, control, rules, label, helperText, solveError, ...textProps}){
    
    return (
        <Controller
            name={name}
            control={control}
            rules={rules}
            render={({
                field: { onChange, value },
                fieldState: { error },
            }) => (
                <FormControl className='form-control' error={!!error}>
                    <TextField
                        label={label}
                        value={value}
                        error={!!error}
                        onChange={(e) => {
                            if (!!error) { 
                                if (!!solveError) { solveError(name);}
                            }
                            onChange(e);
                        }}
                        {...textProps}
                    />
                    {error
                        ? <FormHelperText>{error.message}</FormHelperText>
                        : <FormHelperText>{helperText}</FormHelperText>
                    }
                </FormControl>
            )}
        />
    );
};