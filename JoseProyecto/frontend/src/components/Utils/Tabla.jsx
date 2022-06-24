/* eslint-disable react-hooks/exhaustive-deps */
import * as React from 'react';
import { DataGrid } from '@mui/x-data-grid';
import { Box, Paper, Typography, IconButton } from '@mui/material';
import DeleteIcon from '@mui/icons-material/Delete';
import AutoFixHighIcon from '@mui/icons-material/AutoFixHigh';
import Tooltip, { tooltipClasses } from '@mui/material/Tooltip';
import { styled } from '@mui/material/styles';


const BootstrapTooltip = styled(({ className, ...props }) => (
    <Tooltip {...props} arrow classes={{ popper: className }} />
        ))(({ theme }) => ({
    [`& .${tooltipClasses.arrow}`]: {
        color: theme.palette.common.black,
    },
    [`& .${tooltipClasses.tooltip}`]: {
        backgroundColor: theme.palette.common.black,
    },
}));

export default function Tabla({columns, sendEdit, sendDelete, listado, title}) {    
    const [row, setRow] = React.useState([]);
    const [tableheight, setTableheight] = React.useState(163);
    const [rowSelected, setRowSelected] = React.useState([]);
    React.useEffect(() => {
        setRow(listado);
    }, [listado]);
    React.useEffect(() => {
        if (row.length > 1 && row.length < 9) {
            setTableheight(row.length * 52 + 115);
        }
        else if (row.length > 9) {
            setTableheight(9 * 52 + 115);
        }
        else {
            setTableheight(163);
        }
    },[row.length, setTableheight]);
    return (
        <Box
            sx={{
                alignItems: 'center',
                '& > :not(style)': { m:'48px 8px 8px 8px' },
                width:'100%',
            }}
            >
            <Paper elevation={3} sx={{ p: 2,width: 'calc(100%-32px)' }}>
                <Typography gutterBottom={false} variant='h6' className='card-title' sx={{
                    fontSize:{ xs:'1.2em', md:'1.5em'},
                    }}>
                    { rowSelected.length>0
                        ?<div style={{ display: 'flex', flexGrow: 1 }} >
                            <div style={{ display: 'flex', flexGrow: 1 }}>Seleccionados: {rowSelected.length} </div>
                            {rowSelected.length === 1 &&
                                <div style={{ display: 'flex', flexGrow: 0, mr: 2 }}>
                                    <BootstrapTooltip title="Editar" placement='top'>
                                        <IconButton
                                            size='small'
                                            onClick={() => {                                                
                                                sendEdit(rowSelected[0]);
                                            }}
                                            color="inherit"
                                        >
                                            <AutoFixHighIcon />
                                        </IconButton>
                                    </BootstrapTooltip>
                                </div>
                            }
                            <div style={{ display: 'flex', flexGrow: 0 }}>
                                <BootstrapTooltip title="Eliminar" placement='top'>
                                    <IconButton
                                        size='small'
                                        onClick={() => {                                            
                                            sendDelete(rowSelected);
                                        }}
                                        color="inherit"
                                    >
                                        <DeleteIcon />
                                    </IconButton>
                                </BootstrapTooltip>
                            </div>
                        </div>
                        :<div>{title}</div>
                    }
                </Typography>
                <Box sx={{ alignItems: 'center', width: '100%', height:tableheight+'px'}}>
                    <DataGrid
                        rows={row}
                        columns={columns}
                        pageSize={9}
                        rowsPerPageOptions={[9]}
                        checkboxSelection
                        disableSelectionOnClick
                        onSelectionModelChange={(newSelection) => {                            
                            setRowSelected(newSelection);
                        }}
                    />
                </Box>
            </Paper>
        </Box>
    );
}

