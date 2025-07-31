const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const CopyWebpackPlugin = require('copy-webpack-plugin');

module.exports = {
  entry: './src/index.tsx', // Төслийн орох цэг
  output: {
    path: path.resolve(__dirname, 'dist'),
    filename: 'bundle.js', // Гарах файлын нэр
  },
  module: {
    rules: [
      {
        test: /\.(ts|tsx)$/, // .ts эсвэл .tsx өргөтгөлтэй файлыг
        use: 'ts-loader', // ts-loader ашиглан хөрвүүлнэ
        exclude: /node_modules/,
      },
      {
        test: /\.css$/, // .css өргөтгөлтэй файлыг
        use: ['style-loader', 'css-loader'], // style-loader, css-loader ашиглана
      },
      {
        test: /\.(png|svg|jpg|jpeg|gif)$/i,
        type: 'asset/resource',
      }
    ],
  },
  resolve: {
    extensions: ['.tsx', '.ts', '.js'], // Файл импортлоход эдгээр өргөтгөлүүдийг автоматаар хайна
  },
  plugins: [
    new HtmlWebpackPlugin({
      template: './public/index.html', // Загвар болгож ашиглах HTML файл
    }),
    new CopyWebpackPlugin({
      patterns: [
        {
          from: 'public',
          globOptions: {
            ignore: ['**/index.html'],
          },
        },
      ],
    }),
  ],
  devServer: {
    static: {
      directory: path.join(__dirname, 'dist'),
    },
    compress: true,
    port: 3000, // Хөгжүүлэлтийн сервер ажиллах порт
  },
};