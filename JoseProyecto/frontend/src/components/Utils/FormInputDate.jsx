import * as React from 'react';
import { TextField} from '@mui/material';
import { FormControl, FormHelperText} from '@mui/material';
import { Controller } from "react-hook-form";
import AdapterDateFns from '@mui/lab/AdapterDateFns';
import LocalizationProvider from '@mui/lab/LocalizationProvider';
import MobileDatePicker from '@mui/lab/MobileDatePicker'; 
import enUS from "date-fns/locale/en-US";



export default function FormInputText({ name, control,setValue, rules, label, helperText, solveError, ...dateProps }) {
    
    return (
        <Controller
            name={name}
            control={control}
            rules={rules}
            render={({
                field: { value },
                fieldState: { error },
            }) => (
                <FormControl className='form-control' error={!!error}>
                    <LocalizationProvider dateAdapter={AdapterDateFns} locale={enUS}>
                        <MobileDatePicker
                            label={label}
                            name={name}
                            value={value}
                            onChange={(newValue) => {
                                setValue(name, newValue , {shouldValidate:true, shouldDirty:true})
                                if (!!error) { 
                                    if (!!solveError) { solveError(name);}
                                }
                            }}
                            renderInput={(params) => <TextField                                
                                {...params}
                                error={Boolean(!!error)}
                            />}
                            {...dateProps}
                        />
                    </LocalizationProvider>
                    {error
                        ? <FormHelperText>{error.message}</FormHelperText>
                        : <FormHelperText>{helperText}</FormHelperText>
                    }
                </FormControl>
            )}
        />
    );
};