import * as React from 'react';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import Typography from '@mui/material/Typography';
import { CardActionArea } from '@mui/material';

export default function Cardinicio() {
  return (
    <Card sx={{ width:'100%', marginTop:2, boxShadow: 3}}>
      <CardActionArea>
        <CardMedia
          component="img"
          height="340"
          image="/universidad.jpg"
          alt="Universidad de Camagüey"
        />
        <CardContent>
          <Typography gutterBottom variant="h1" sx={{
            fontSize:{ xs:'1.7em', md:'3em'},
            textAlign: 'center',
            fontWeight:'450'
            }}>
            Aplicación de Postgrados
          </Typography>
          <Typography variant="body2" color="text.secondary"sx={{
            fontSize:{ xs:'1em', md:'1.5em'},
            textAlign: { xs:'justify', sm:'center'},
            }}>
            Aplicación encargada de la gestión de postgrados nacionales e internacionales, con sus estudiantes y profesores.
            Brinda varios reportes, con el fin de encontrar y calcular los datos requeridos en los mismos.
          </Typography>
        </CardContent>
      </CardActionArea>
    </Card>
  );
}