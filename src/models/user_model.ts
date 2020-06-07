import BaseModel from "./base_model.ts";

export type UserEntity = {
  bio?: string;
  email: string;
  id?: number;
  image?: string;
  password?: string;
  username: string;
  token?: null | string;
};

export function createUserModelObject(user: any): UserModel {
  return new UserModel(
    user.username,
    user.password,
    user.email,
    user.bio,
    user.image,
    user.id,
  );
}

export class UserModel extends BaseModel {
  //////////////////////////////////////////////////////////////////////////////
  // FILE MARKER - PROPERTIES //////////////////////////////////////////////////
  //////////////////////////////////////////////////////////////////////////////

  public bio: string;
  public email: string;
  public id: number;
  public image: string;
  public password: string;
  public username: string;

  //////////////////////////////////////////////////////////////////////////////
  // FILE MARKER - CONSTRCUTOR /////////////////////////////////////////////////
  //////////////////////////////////////////////////////////////////////////////

  constructor(
    username: string,
    password: string,
    email: string,
    bio: string = "",
    image: string = "https://static.productionready.io/images/smiley-cyrus.jpg",
    id: number = -1,
  ) {
    super();
    this.id = id;
    this.username = username;
    this.password = password;
    this.email = email;
    this.bio = bio;
    this.image = image;
  }

  //////////////////////////////////////////////////////////////////////////////
  // FILE MARKER - METHODS - STATIC ////////////////////////////////////////////
  //////////////////////////////////////////////////////////////////////////////

  /**
   * Get records using the WHERE clause.
   *
   * @param any fields
   */
  static async where(fields: any): Promise<UserModel | null> {
    let query = "SELECT * FROM users WHERE ";
    let clauses: string[] = [];
    for (let field in fields) {
      let value = fields[field];
      clauses.push(`${field} = '${value}'`);
    }
    query += clauses.join(" AND ");

    const client = await BaseModel.connect();
    const dbResult = await client.query(query);
    client.release();

    let results: any = BaseModel.formatResults(
      dbResult.rows,
      dbResult.rowDescription.columns,
    );

    if (results && results.length > 0) {
      return createUserModelObject(results[0]);
    }

    return null;
  }

  /**
   * Get records by the given id column values.
   *
   * @param number[] ids
   */
  static async whereIn(column: string, values: number[]) {
    if (values.length <= 0) {
      return [];
    }

    let query = `SELECT * FROM users WHERE ${column} IN (${values.join(",")});`;

    const client = await BaseModel.connect();
    const dbResult = await client.query(query);
    client.release();

    let users: any = BaseModel.formatResults(
      dbResult.rows,
      dbResult.rowDescription.columns,
    );
    if (users && users.length > 0) {
      return users.map((user: any) => {
        return createUserModelObject(user);
      });
    }

    return [];
  }

  /**
   * Get a record by the username column value.
   *
   * @param string username
   */
  static async whereUsername(username: string) {
    const query = `SELECT * FROM users WHERE username = '${username}';`;

    const client = await BaseModel.connect();
    const dbResult = await client.query(query);
    client.release();

    const user = BaseModel.formatResults(
      dbResult.rows,
      dbResult.rowDescription.columns,
    );
    if (user && user.length > 0) {
      return createUserModelObject(user[0]);
    }

    return null;
  }

  //////////////////////////////////////////////////////////////////////////////
  // FILE MARKER - METHODS - PUBLIC ////////////////////////////////////////////
  //////////////////////////////////////////////////////////////////////////////

  /**
   * Delete this model.
   *
   * @return Promise<boolean>
   */
  public async delete(): Promise<boolean> {
    let query = `DELETE FROM users WHERE id = ?`;
    query = this.prepareQuery(
      query,
      [
        String(this.id),
      ],
    );

    try {
      const client = await BaseModel.connect();
      await client.query(query);
      client.release();
    } catch (error) {
      console.log(error);
      return false;
    }
    return true;
  }

  /**
   * Save this model.
   *
   * @return Promise<UserModel>
   */
  public async save(): Promise<UserModel> {
    // If this model already has an ID, then that means we're updating the model
    if (this.id != -1) {
      return this.update();
    }

    let query = "INSERT INTO users " +
      " (username, email, password, bio, image)" +
      " VALUES (?, ?, ?, ?, ?);";
    query = this.prepareQuery(
      query,
      [
        this.username,
        this.email,
        this.password,
        this.bio,
        this.image,
      ],
    );

    const client = await BaseModel.connect();
    await client.query(query);
    client.release();

    // @ts-ignore
    // (crookse) This will never return null.
    return UserModel.where({email: this.email});
  }

  /**
   * Update this model.
   *
   * @return Promise<UserModel>
   */
  public async update(): Promise<UserModel> {
    let query = "UPDATE users SET " +
      "username = ?, password = ?, email = ?, bio = ?, image = ? " +
      `WHERE id = '${this.id}';`;
    query = this.prepareQuery(
      query,
      [
        this.username,
        this.password,
        this.email,
        this.bio,
        this.image,
      ],
    );
    const client = await BaseModel.connect();
    await client.query(query);
    client.release();

    // @ts-ignore
    // (crookse) This will never return null.
    return UserModel.where({email: this.email});
  }

  /**
   * Convert this object to an entity.
   *
   * @return UserEntity
   */
  public toEntity(): UserEntity {
    return {
      id: this.id,
      username: this.username,
      email: this.email,
      bio: this.bio,
      image: this.image,
      token: null,
    };
  }
}

export default UserModel;
