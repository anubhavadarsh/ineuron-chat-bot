const configs = {
  local: {
    ApiBaseUrl: "http://localhost:5000",
  },
  development: {
    ApiBaseUrl: "http://3.141.196.137:80",
  },
  prod: {
    ApiBaseUrl: "",
    AppDomain: "",
  },
};

const environment = process.env.NODE_ENV;
const config = configs[environment];

export default config;
