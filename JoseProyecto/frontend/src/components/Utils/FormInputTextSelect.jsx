import * as React from 'react';
import { TextField} from '@mui/material';
import { FormControl, FormHelperText, MenuItem} from '@mui/material';
import { Controller} from "react-hook-form";

export default function FormInputTextSelect({ name, control, rules, label, options, helperText, solveError}){
    
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
                        select
                        error={!!error}
                        value={value}
                        onChange={(e) => { 
                            if (!!error) { 
                                if (!!solveError) { solveError(name);}
                            }
                            onChange(e);
                        }}
                    >
                        {options.map((option) => (
                            <MenuItem key={option} value={option}>
                            {option}
                            </MenuItem>
                        ))}
                    </TextField>
                    {error
                        ? <FormHelperText>{error.message}</FormHelperText>
                        : <FormHelperText>{helperText}</FormHelperText>
                    }
                </FormControl>
            )}
        />
    );
};
